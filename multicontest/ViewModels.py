"""
This file is part of MultiConTest.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

__author__ = "Nicolas Kersten"
__license__ = 'GNU General Public License v3.0'

import math
import webbrowser

import numpy as np
import pandas as pd
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt, QUrl
from PySide6.QtWidgets import QWidget, QDialog, QTableView
from matplotlib import ticker as mtick, cm
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from multicontest.AboutDialog import Ui_about_dialog


class SimplePandasModel(QAbstractTableModel):

    def __init__(self, parent: QTableView, first_num_col: int or None = 1, last_num_col: int = None,
                 n_digits: int = 4, scientific_notation: bool = False, nan_value: str = None):
        """ Constructor: Table model for pandas DataFrame
        :param parent: parent widget -> QTableView
        :param first_num_col: first column with numeric values -> used to determine columns for numeric formatting
        :param last_num_col: last column with numeric values -> used to determine columns for numeric formatting
        :param n_digits: number of digits to round to
        :param scientific_notation: use scientific notation
        :param nan_value: string to display for NaN values
        """
        super().__init__(parent)
        self.table = parent
        self._data = pd.DataFrame()
        self.first_num_col = first_num_col
        self.last_num_col = last_num_col
        self.round_digits = n_digits
        self.scientific_notation = scientific_notation
        self.nan_value = nan_value

    def rowCount(self, parent=QModelIndex()) -> int:
        """ Override method from QAbstractTableModel
        Return row count of the pandas DataFrame
        """
        if parent == QModelIndex():
            return self._data.shape[0]

        return 0

    def columnCount(self, parent=QModelIndex):
        """Override method from QAbstractTableModel
        Return column count of the pandas DataFrame
        """
        if parent == QModelIndex():
            return self._data.shape[1]
        return 0

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            if self.first_num_col is not None and isinstance(value, float) and index.column() >= self.first_num_col:
                if self.last_num_col is None or self.last_num_col >= index.column():
                    if self.scientific_notation:
                        return f'{value:.{self.round_digits}g}' if not math.isnan(value) else self.nan_value
                    if value == 0:
                        return "0"
                    elif abs(value) > 10 ** -self.round_digits:
                        return str(round(value, ndigits=self.round_digits))
                    elif math.isnan(value):
                        return self.nan_value
                    else:
                        return f'< e-{self.round_digits}'
            if value is None or isinstance(value, float) and math.isnan(value):
                return self.nan_value
            return str(value)
        if role == Qt.TextAlignmentRole:
            if self.first_num_col is not None:
                if self.last_num_col is None:
                    if index.column() >= self.first_num_col:
                        return Qt.AlignRight + Qt.AlignVCenter
                else:
                    if self.last_num_col >= index.column() >= self.first_num_col:
                        return Qt.AlignRight + Qt.AlignVCenter
            return Qt.AlignLeft + Qt.AlignVCenter

        return None

    def set_data(self, data: pd.DataFrame):
        self._data = data
        self.layoutChanged.emit()
        self.dataChanged.emit(QModelIndex(), QModelIndex())
        self.table.resizeColumnsToContents()

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            if orientation == Qt.Vertical:
                return str(self._data.index[section])
        if role == Qt.TextAlignmentRole:
            if orientation == Qt.Horizontal:
                return Qt.AlignLeft + Qt.AlignVCenter
            if orientation == Qt.Vertical:
                return Qt.AlignLeft + Qt.AlignVCenter
        return None

    def get_current_data_index(self):
        return self._data.index[self.table.currentIndex().row()]

    def get_data_by_index(self, index: int):
        return self._data.index[index]

    def select_by_name(self, name: str):
        if name not in self._data.index:
            return False
        index = self._data.index.get_loc(name)
        self.table.selectRow(index)
        return True

    def clear(self):
        self.set_data(pd.DataFrame())


class MatplotlibCanvas(FigureCanvasQTAgg):

    def __init__(self, dpi=120):
        self.fig = Figure(dpi=dpi, tight_layout=True)
        self.axes = self.fig.add_subplot(111)
        super(MatplotlibCanvas, self).__init__(self.fig)


class MPLStackedBarChart(QWidget):

    def __init__(self, controller, parent=None, dpi=120):
        """Constructor: Stacked bar chart widget
        :param controller: Controller instance
        :param parent: parent widget
        :param dpi: dpi of the matplotlib figure
        """
        QWidget.__init__(self, parent=parent)
        self.controller = controller
        self.figure = MatplotlibCanvas(dpi=dpi)
        self.data = None
        self.labels = None
        self.title = None
        self.title_size = 12
        self.x_label_size = 8
        self.y_label_size = 8
        self.x_label = None
        self.y_label = None
        self.x_rotation = 0
        self.y_rotation = 0
        self.x_tick_size = 6
        self.y_tick_size = 8

    def set_data(self, data: dict, labels: list, x_label: str, y_label: str, title: str = None):
        self.data = data
        self.labels = labels
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.draw_figure()

    def draw_figure(self):
        if self.data is None:
            self.clear()
            return
        figure = self.figure
        axes = self.figure.axes
        self.clear()
        cmap = cm.get_cmap("tab20") if len(self.data) > 10 else cm.get_cmap("tab10")
        colors = {label: cmap(i) for i, label in enumerate(self.data)}
        previous = np.zeros(len(self.labels))
        for label, values in self.data.items():
            axes.bar(values[0], values[1], label=label, bottom=previous, align="center", color=colors[label])
            previous += values[1]
        axes.set_xticks(list(range(len(previous))))
        axes.set_xticklabels(self.labels)
        axes.yaxis.set_major_formatter(mtick.PercentFormatter())

        axes.tick_params(axis="x", labelrotation=self.x_rotation, labelsize=self.x_tick_size, which='major',
                         bottom=True, top=False, labelbottom=True)
        axes.tick_params(axis="y", labelsize=self.y_tick_size, which='both', labelleft=True, left=True,
                         labelrotation=self.y_rotation)

        axes.set_title(self.title, fontsize=self.title_size)

        axes.set_xlabel(self.x_label, fontsize=self.x_label_size)
        axes.set_ylabel(self.y_label, fontsize=self.y_label_size)

        axes.legend(bbox_to_anchor=(1.04, 1), loc="upper left")

        figure.draw()

    def clear(self):
        self.figure.axes.clear()
        self.figure.draw()


class About(QDialog, Ui_about_dialog):

    def __init__(self, version: str, website_link: str, doc_link: str):
        super(About, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowTitle("About MultiConTest")
        self.close_btn.clicked.connect(self.close)
        self.website_btn.clicked.connect(lambda: webbrowser.open(website_link))
        self.doc_btn.clicked.connect(lambda: webbrowser.open(doc_link))
        self.version_label.setText(f"Version {version}")
        self.license_text.setSource(QUrl("qrc:/license/license_text.html"))
        self.opensource_text.setSource(QUrl("qrc:/license/opensource_package_licenses.html"))
