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

import webbrowser

import pandas as pd
from PySide6.QtCore import Qt, QStringListModel
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QFileDialog, QVBoxLayout, QMessageBox, QCompleter, QFrame, QCheckBox

from multicontest.MainWindow import Ui_MainWindow as MainUI
from multicontest.ViewModels import SimplePandasModel, MPLStackedBarChart, About


class MainView(QMainWindow, MainUI):
    figure_x_label = "Cluster"
    figure_y_label = "Percentage of samples"
    figure_title = "Per-cluster label distribution"

    def __init__(self, controller, version: str):
        super().__init__()
        self.setupUi(self)
        self.controller = controller
        self.controller.view = self
        self.version = version
        self.setWindowTitle("MultiConTest " + self.version)
        self.controller.app.setWindowIcon(QIcon(":/icons/multicontest_icon.png"))
        self.warning_icon = QIcon(":/icons/multicontest_warning.png")
        self.question_icon = QIcon(":/icons/multicontest_question.png")
        self.website_link = "http://pfeiferlab.org/research/our-software/"
        self.documentation_link = "https://github.com/pfeiferAI/MultiConTest"
        self.web_rmkl_link = "https://www.web-rmkl.org"
        self.publication_link = "https://doi.org/10.1101/2022.10.14.512210"
        self.advanced_hidden = False
        self.query_enabled = False
        self.p_val_details_visible = False
        self.setup_view()
        self.setup_interactions()

    def setup_view(self):
        self.cls_unique_table_model = SimplePandasModel(self.cls_unique_table, first_num_col=0)
        self.cls_unique_table.setModel(self.cls_unique_table_model)

        self.cls_table_model = SimplePandasModel(self.cls_table)
        self.cls_table.setModel(self.cls_table_model)

        self.label_table_model = SimplePandasModel(self.label_table, first_num_col=None)
        self.label_table.setModel(self.label_table_model)

        self.cont_table_model = SimplePandasModel(self.cont_table, first_num_col=0)
        self.cont_table.setModel(self.cont_table_model)

        self.results_table_model = SimplePandasModel(self.results_table, first_num_col=0,
                                                     last_num_col=2, scientific_notation=True, n_digits=4)
        self.results_table.setModel(self.results_table_model)

        self.conf_chart_layout = QVBoxLayout()
        self.conf_chart_layout.setContentsMargins(0, 0, 0, 0)
        self.conf_vis_widget.setLayout(self.conf_chart_layout)
        self.conf_chart = MPLStackedBarChart(self.controller)
        self.conf_chart_layout.addWidget(self.conf_chart.figure)
        self.results_tab.hide()
        self.tabWidget.setTabVisible(3, False)
        self.conf_tab.setDisabled(True)

        self.enable_cls_details(False)
        self.enable_label_import(False)
        self.enable_label_selection_vis(False)
        self.enable_confounding_test(False)
        self.show_confounding_warning(False)
        self.show_progress(False)
        self.export_single_result_btn.hide()
        self.show_confounding_details(show=False)
        self.perm_frame_warning.hide()
        self.p_val_details_btn.hide()

        self.show_advanced()
        self.enable_export(False)
        self.update_category_threshold()

        self.completer_data_model = QStringListModel()
        self.completer = QCompleter(self.completer_data_model)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.setFilterMode(Qt.MatchContains)
        self.completer.setCompletionColumn(0)
        self.query_field.setCompleter(self.completer)
        self.completer.popup().setFrameShape(QFrame.Panel)

        self.show_category_query(False)

    def setup_interactions(self):
        self.select_cls_file.clicked.connect(self.import_clustering)
        self.import_labels_btn.clicked.connect(self.import_sample_labels)
        self.advanced_label_settings_btn.clicked.connect(self.show_advanced)
        self.refine_cat_count_btn.clicked.connect(lambda: self.warn_and_update_categories(replace=False,
                                                                                          sender="btn"))
        self.drop_missing_check.stateChanged.connect(lambda: self.warn_and_update_categories(replace=True,
                                                                                             sender="check"))
        self.find_cat_btn.clicked.connect(self.enable_category_query)
        self.generate_clustering_btn.clicked.connect(self.show_clustering_options)
        self.conf_compute_btn.clicked.connect(self.controller.compute_multicontest)
        self.p_val_details_btn.clicked.connect(lambda: self.show_confounding_details())
        self.export_single_result_btn.clicked.connect(self.export_single_result)
        self.export_all_results_btn.clicked.connect(lambda: self.export_results(all_results=True))
        self.action_export_test_result.triggered.connect(self.export_single_result)
        self.action_export_all_results.triggered.connect(lambda: self.export_results(all_results=True))

        self.label_table.selectionModel().selectionChanged.connect(self.select_current_label)
        self.sort_up_btn.clicked.connect(lambda: self.controller.sort_labels(ascending=True))
        self.sort_down_btn.clicked.connect(lambda: self.controller.sort_labels(ascending=False))

        self.completer.highlighted.connect(self.label_table_model.select_by_name)
        self.completer.activated.connect(self.accecpt_completion)

        self.action_about.triggered.connect(self.show_about)
        self.action_method_description.triggered.connect(lambda: webbrowser.open(self.publication_link))
        self.action_software_description.triggered.connect(lambda: webbrowser.open(self.documentation_link))
        self.action_clear_all.triggered.connect(self.clear_view)

    # enable or disable view functions

    def enable_cls_details(self, enable: bool):
        self.cls_details_frame.setEnabled(enable)

    def enable_label_import(self, enable: bool):
        self.import_labels_btn.setEnabled(enable)

    def enable_label_selection_vis(self, enable: bool):
        self.label_selection_frame.setEnabled(enable)
        self.advanced_label_settings_btn.setEnabled(enable)

    def enable_label_modification(self, enable: bool):
        self.tabWidget.setTabEnabled(1, enable)

    def enable_confounding_test(self, enable: bool):
        self.conf_compute_btn.setEnabled(enable)

    def enable_export(self, enable: bool):
        self.action_export_test_result.setEnabled(enable)
        self.action_export_all_results.setEnabled(enable)

    def show_confounding_details(self, show: bool = None, clear: bool = False):
        if clear:
            self.orig_p_val_frame.setVisible(False)
            self.orig_p_txt.setText("")
            self.perm_frame.setVisible(False)
            self.failed_perm_txt.setText("")
            self.perm_frame_warning.setVisible(False)
            self.failed_perm_txt_warning.setText("")
            self.p_val_details_btn.setText("Show details")
            return
        if show is None:
            show = not self.p_val_details_visible
        self.p_val_details_visible = show
        self.orig_p_val_frame.setVisible(show)
        show_permutations = show and not self.perm_frame_warning.isVisible()
        self.perm_frame.setVisible(show_permutations)
        if show:
            self.p_val_details_btn.setText("Hide details")
        else:
            self.p_val_details_btn.setText("Show details")

    def show_advanced(self):
        self.cat_advanced_frame.setVisible(self.advanced_hidden)
        if self.advanced_hidden:
            self.advanced_label_settings_btn.setText("Hide category adjustments")
        else:
            self.advanced_label_settings_btn.setText("Adjust categories")
        self.advanced_hidden = not self.advanced_hidden

    def show_clustering_options(self):
        webbrowser.open(self.web_rmkl_link)

    def show_warning(self, title: str, message: str = None):
        if message is None:
            message = title
            title = "Warning"
        box = QMessageBox(self)
        box.setIconPixmap(self.warning_icon.pixmap(50, 50))
        box.setWindowTitle(title)
        box.setText(message)
        box.setStandardButtons(QMessageBox.Ok)
        box.exec()

    def show_confounding_warning(self, value: bool):
        self.conf_warning_frame.setVisible(value)

    def show_progress(self, value: bool):
        if value and self.progress_bar.isHidden():
            self.progress_bar.setValue(0)
        self.progress_bar.setVisible(value)

    def clear_label_table(self):
        self.label_table_model.clear()

    def show_sorting(self, value: bool):
        self.sort_frame.setVisible(value)

    def show_category_query(self, value: bool):
        self.query_field.setVisible(value)
        self.show_sorting(not value)
        if value:
            self.find_cat_btn.setText("Cancel")
        else:
            self.query_field.setText("")
            self.find_cat_btn.setText("Find label")

    def enable_category_query(self):
        value = not self.query_enabled
        self.query_enabled = value
        self.show_category_query(value)

    def show_about(self):
        diag = About(version=self.version, website_link=self.website_link, doc_link=self.documentation_link)
        diag.exec()

    def show_publication(self):
        webbrowser.open(self.publication_link)

    # view functions

    def select_current_label(self):
        self.controller.select_label(self.label_table_model.get_current_data_index())
        self.conf_tab.setDisabled(False)

    def accecpt_completion(self, name: str):
        if self.label_table_model.select_by_name(name):
            self.show_category_query(False)
            self.query_enabled = False

    def warn_and_update_categories(self, replace: bool, sender: str):
        if self.controller.test_count > 0:
            accept = self.ask_question("Available sample label update",
                                       "Refining the category settings will change the number of available sample "
                                       "labels. Already computed test results will be deleted. Do you want to "
                                       "continue?")
        else:
            accept = True
        if accept:
            cat_threshold = self.category_count_spin.value() if sender == "btn" else None
            print(cat_threshold)
            self.controller.update_categories(replace=replace, category_threshold=cat_threshold)
        else:
            if sender == "btn":
                self.update_category_threshold()
            elif sender == "check":
                current_state = self.drop_missing_check.isChecked()
                self.drop_missing_check.setChecked(not current_state)

    def import_clustering(self):
        if self.controller.has_cluster_data:
            clear_continue, export = self.show_overwrite_warning(clustering=True,
                                                                 export_result=self.controller.test_count > 0)
            if clear_continue:
                if export:
                    self.export_results(all_results=True)
                self.controller.clear_all_data()
            else:
                return
        name, _ = QFileDialog.getOpenFileName(self, "Open Clustering", self.controller.current_dir,
                                              "CSV/TXT Files (*.csv *.CSV *.txt *.TXT)")
        if name is None or len(name) == 0:
            return
        with_header = self.ask_question("Clustering file format",
                                        "Does your clustering file contain a header line?")
        self.controller.load_clustering(name, with_header)

    def import_sample_labels(self):
        name, _ = QFileDialog.getOpenFileName(self, "Open Sample Labels", self.controller.current_dir,
                                              "CSV Files (*.csv *.CSV)")
        if name is None or len(name) == 0:
            return
        self.controller.load_test_labels(name)

    def export_single_result(self):
        if self.controller.test_count == 0:
            return
        if self.controller.test_count == 1:
            self.export_results(all_results=False)
            return
        self.export_results(all_results=self.ask_question(
            "Export Single Result", "Do you want to export all results instead of just the selected one?"))

    def export_results(self, all_results: bool = True):
        apdx = "s" if all_results else ""
        file_type = "CSV Files (*.csv *.CSV)" if all_results else "TXT Files (*.txt *.TXT)"
        name, _ = QFileDialog.getSaveFileName(self, f"Export MultiContest Result{apdx}", self.controller.current_dir,
                                              file_type)
        if name is None or len(name) == 0:
            return
        self.controller.export_test_results(name, all_results)

    def ask_question(self, title: str, question: str):
        box = QMessageBox(self)
        box.setIconPixmap(self.question_icon.pixmap(50, 50))
        box.setWindowTitle(title)
        box.setText(question)
        box.setStandardButtons(box.StandardButton.Yes | box.StandardButton.No)
        return box.exec() == box.StandardButton.Yes

    def show_overwrite_warning(self, clustering: bool, export_result: bool = False):
        box = QMessageBox(self)
        box.setIconPixmap(self.warning_icon.pixmap(50, 50))
        file_type = "clustering" if clustering else "sample label"
        box.setWindowTitle("Remove existing data?")
        box.setText(f"Remove existing data and import new {file_type} file?")
        box.setInformativeText(f"Importing a new {file_type} file will remove all existing data and computed test "
                               f"results. This cannot be undone! Do you want to continue?")
        box.setStandardButtons(box.StandardButton.Yes | box.StandardButton.No)
        if export_result:
            cbx = QCheckBox("Export existing results before removing all data")
            box.setCheckBox(cbx)
        reply = box.exec()
        if export_result:
            return reply == box.StandardButton.Yes, cbx.isChecked()
        return reply == box.StandardButton.Yes, False

    # view updates

    def update_cluster_view(self, unique_cls_table: pd.DataFrame, all_cls_table: pd.DataFrame,
                            sample_count: int, cluster_count: int, file_name: str):
        self.enable_cls_details(True)
        self.generate_clustering_btn.hide()
        self.cls_file_text.setText(file_name)
        self.sample_count_lbl.setText("Samples")
        self.sample_count_txt.setText(str(sample_count))
        self.cluster_count_txt.setText(str(cluster_count))
        self.cls_unique_table_model.set_data(unique_cls_table)
        self.cls_table_model.set_data(all_cls_table)
        self.enable_label_import(True)

    def update_label_view(self, table: pd.DataFrame, sample_count: int, sample_overlap: int, label_count: int,
                          cat_label_count: int, file_name: str = None, selection_name: str = None):
        if file_name is not None:
            self.label_file_txt.setText(file_name)
        self.overlap_txt.setText(f"{sample_overlap} / {sample_count}")
        self.label_count_txt.setText(str(label_count))
        self.cat_label_txt.setText(str(cat_label_count))
        self.label_table_model.set_data(table)
        self.update_completer(table)
        if selection_name is None:
            current_row = self.label_table.currentIndex().row()
            self.label_table.selectRow(0)
            if current_row == 0:
                self.controller.select_label(self.label_table_model.get_data_by_index(0))
        else:
            self.label_table_model.select_by_name(selection_name)
        self.enable_label_selection_vis(True)
        self.enable_label_import(False)
        self.enable_confounding_test(True)

    def update_completer(self, table: pd.DataFrame):
        self.completer_data_model.setStringList(table.index.tolist())

    def update_current_label(self, current_label: str, overlap: int, sample_count: int, vis_data_dict: dict,
                             x_ticks: list, cont_table: pd.DataFrame, missing_count: int = None):
        self.sample_count_txt.setText(str(overlap))
        self.sample_count_lbl.setText("Available Samples")
        self.conf_factor_txt.setText(current_label)
        self.conf_chart.set_data(vis_data_dict, x_ticks, self.figure_x_label, self.figure_y_label, self.figure_title)
        self.cont_table_model.set_data(cont_table)
        if missing_count is not None and not self.drop_missing_check.isChecked():
            self.sel_overlap_txt.setText(f"{overlap} / {sample_count} (contains {missing_count} missing values)")
        else:
            self.sel_overlap_txt.setText(f"{overlap} / {sample_count}")

    def update_p_value(self, p_value: str, disable_computation: bool = True, details: dict = None):
        self.show_confounding_details(clear=True)
        self.conf_p_val_txt.setText(p_value)
        if details is not None and isinstance(details, dict):
            self.orig_p_txt.setText(f"{details['original_p_value']:.5G}")
            percent_skipped = details["total_n_skipped"] / details["total_n_iter"] * 100
            if percent_skipped > 10:
                self.perm_frame_warning.show()
            self.failed_perm_txt.setText(f"{percent_skipped:.2f}%")
            self.failed_perm_txt_warning.setText(f"{percent_skipped:.2f}%")
            self.p_val_details_btn.show()
            self.export_single_result_btn.show()
        else:
            self.p_val_details_btn.hide()
            self.export_single_result_btn.hide()
        self.enable_confounding_test(not disable_computation)

    def update_test_results(self, results_df: pd.DataFrame):
        self.results_table_model.set_data(results_df)
        if results_df.shape[0] > 1:
            self.tabWidget.setTabVisible(3, True)

    def update_confounding_warning(self, msg: str, show: bool = True):
        self.conf_warning_txt.setText(msg)
        self.show_confounding_warning(show)

    def update_category_threshold(self, value: int = None):
        if value is None:
            value = self.controller.current_category_threshold
        self.category_count_spin.setValue(value)

    def update_progress(self, progress: float):
        self.progress_bar.setValue(progress)

    # access view data

    def get_max_categories(self):
        return self.category_count_spin.value()

    def get_drop_nan_categories(self):
        return self.drop_missing_check.isChecked()

    # clear view
    def clear_view(self):
        self.cls_unique_table_model.clear()
        self.cls_table_model.clear()
        self.label_table_model.clear()
        self.cont_table_model.clear()
        self.results_table_model.clear()
        self.conf_chart.clear()

        self.results_tab.hide()
        self.tabWidget.setTabVisible(3, False)
        self.conf_tab.setDisabled(True)

        self.enable_cls_details(False)
        self.enable_label_import(False)
        self.enable_label_selection_vis(False)
        self.enable_confounding_test(False)
        self.show_confounding_warning(False)
        self.show_progress(False)
        self.export_single_result_btn.hide()
        self.show_confounding_details(show=False)
        self.perm_frame_warning.hide()
        self.p_val_details_btn.hide()
        self.enable_export(False)
        self.show_category_query(False)

        self.select_cls_file.setEnabled(True)
        self.generate_clustering_btn.show()

        self.cls_file_text.setText("No file selected")
        self.sample_count_txt.setText("0")
        self.cluster_count_txt.setText("0")
        self.label_count_txt.setText("0")
        self.cat_label_txt.setText("0")
        self.label_file_txt.setText("No file selected")
        self.overlap_txt.setText("--")
        self.sel_overlap_txt.setText("--")
        self.conf_warning_txt.setText("--")
        self.conf_factor_txt.setText("--")
        self.conf_p_val_txt.setText("not computed")
        self.orig_p_txt.setText("")
        self.failed_perm_txt.setText("")
        self.failed_perm_txt_warning.setText("")
