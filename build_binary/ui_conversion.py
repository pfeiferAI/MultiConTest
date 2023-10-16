"""
This script converts the Qt Designer .ui files to Python code using PySide6. This code has to be run from the
project build directory. The file names are specific to MultiConTest.

This file is part of MultiConTest

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

import os

ui_file_dict = {
    "MainWindow.ui": "MainWindow.py",
    "AboutDialog.ui": "AboutDialog.py"
}

qrc_file_dict = {
    "resources.qrc": "resources_rc.py",
}

if __name__ == "__main__":
    if not os.path.exists("../res") and not os.path.exists("../src"):
        print("Please run this script from the project build directory.")
        exit(1)
    for ui_file, py_file in ui_file_dict.items():
        ui_file_path = os.path.join("../res", ui_file)
        py_file_path = os.path.join("../multicontest", py_file)
        os.system("pyside6-uic -o %s %s" % (py_file_path, ui_file_path))
        # replace resource import statement to make the file compatible with the package structure
        with open(py_file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            if "import resources_rc" in line:
                lines[i] = "from multicontest import resources_rc\n"
                break
        with open(py_file_path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print("Converted %s to %s" % (ui_file, py_file))
    for qrc_file, py_file in qrc_file_dict.items():
        qrc_file_path = os.path.join("../res", qrc_file)
        py_file_path = os.path.join("../multicontest", py_file)
        os.system("pyside6-rcc -o %s %s" % (py_file_path, qrc_file_path))
        print("Converted %s to %s" % (qrc_file, py_file))
    print("Done.")
    exit(0)
