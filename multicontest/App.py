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
__version__ = "1.0"

import sys

from PySide6.QtCore import QFile
from PySide6.QtWidgets import QApplication

from multicontest.Controller import Controller
from multicontest.View import MainView


class App(QApplication):
    """Main entry point for MultiConTest App"""

    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        self.init_style()
        self.controller = Controller(self)
        self.main_view = MainView(self.controller, __version__)
        self.main_view.show()

    def init_style(self):
        style = QFile(":/style/multicontest_style.qss")
        style.open(QFile.ReadOnly)
        style_sheet = str(style.readAll(), encoding="utf-8")
        style.close()
        # set font size to 10pt on Windows and Linux, 13pt on macOS to account for different default DPI settings
        if not sys.platform.startswith("darwin"):
            normal_font_size = 10
        else:
            normal_font_size = 13
        style_sheet = f"* {{font-family: Arial; font-size: {normal_font_size}pt; color: #e6e9ed;}}\n" + style_sheet
        self.setStyleSheet(style_sheet)


def main():
    app = App(sys.argv)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
