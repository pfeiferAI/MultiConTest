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

import os
from pathlib import Path

import pandas as pd
from PySide6.QtCore import QThreadPool

from multicontest.ConfounderTest import run_confounding_test
from multicontest.DataModel import DataModel


class Controller:

    def __init__(self, app):
        self.app = app
        self.view = None  # is set by the view
        self.data_model = DataModel(self)
        self.current_dir = str(Path.home())
        self.selected_label = None
        self.threadpool = QThreadPool()
        self.current_worker = None
        self.test_count = 0

    @property
    def drop_nan_categories(self):
        return self.view.get_drop_nan_categories()

    @property
    def current_category_threshold(self):
        return self.data_model.selected_category_threshold

    @property
    def has_cluster_data(self):
        return not self.data_model.raw_cls_data.empty

    def load_clustering(self, file_name: str, with_header: bool):
        if file_name is None or len(file_name) == 0:
            return
        self.current_dir = str(Path(file_name).parent)
        try:
            cls_file = pd.read_csv(file_name, index_col=0, header=0 if with_header else None)
        except (pd.errors.ParserError, UnicodeDecodeError, ValueError, FileNotFoundError):
            self.view.show_warning("Could not load clustering file!\n"
                                   "Please check the file format and try again.\n"
                                   "If this issue persists, you may try to save the csv file with utf-8 encoding.")
        try:
            cls_count, sample_count = self.data_model.set_and_validate_clustering(cls_file)
        except ValueError as e:
            self.view.show_warning("Clustering validation failed!\n" + str(e))
            return
        self.view.update_cluster_view(self.data_model.unique_cls_data, self.data_model.preview_cls_data, sample_count,
                                      cls_count, os.path.basename(file_name))

    def load_test_labels(self, file_name: str):
        if file_name is None or len(file_name) == 0:
            return
        self.current_dir = str(Path(file_name).parent)
        try:
            label_file = pd.read_csv(file_name, index_col=0)
        except (pd.errors.ParserError, UnicodeDecodeError, ValueError, FileNotFoundError):
            self.view.show_warning("Could not load label file!\n"
                                   "Please check the file format and try again.\n"
                                   "If this issue persists, you may try to save the csv file with utf-8 encoding.")
        try:
            self.data_model.set_and_validate_labels(label_file)
        except ValueError as e:
            self.view.show_warning("Label validation failed!\n" + str(e))
        else:
            self.update_categories(os.path.basename(file_name))

    def export_test_results(self, file_name: str, all_results: bool):
        if file_name is None or len(file_name) == 0:
            return
        if all_results:
            export_data = self.data_model.results_table
            sep = ","
            header = True
        else:
            export_data = self.data_model.get_current_result_table(self.selected_label)
            sep = "\t"
            header = False
        if export_data is not None and not export_data.empty:
            export_data.to_csv(file_name, sep=sep, header=header)
        else:
            self.view.show_warning("No results to export!")

    def update_categories(self, file_name: str = None, replace: bool = False, keep_results: bool = False,
                          category_threshold: int = None):
        if category_threshold is not None and isinstance(category_threshold, int):
            self.data_model.selected_category_threshold = category_threshold
        if keep_results:
            selection_name = self.selected_label
        else:
            selection_name = None
            self.reset_results()
        if replace:
            self.data_model.generate_label_count_data()
        if not isinstance(file_name, str):
            file_name = None
        self.view.update_label_view(
            table=self.data_model.reduced_label_count_data,
            sample_count=self.data_model.total_sample_count,
            sample_overlap=self.data_model.sample_overlap,
            label_count=self.data_model.total_label_count,
            cat_label_count=self.data_model.reduced_label_count,
            file_name=file_name,
            selection_name=selection_name)

    def select_label(self, label_name: str):
        self.selected_label = label_name
        overlap_labels, missing_count = self.data_model.get_overlap(label_name)
        overlap = len(overlap_labels)
        if self.drop_nan_categories:
            missing_count = None
        vis_data_dict, x_ticks = self.data_model.get_vis_data(label_name)
        cont_table = self.data_model.get_contingency_table(label_name)
        self.view.update_current_label(label_name, overlap, self.data_model.total_sample_count,
                                       vis_data_dict, x_ticks, cont_table, missing_count=missing_count)
        p_txt, error = self.data_model.get_p_value(label_name)
        details = self.data_model.get_detailed_results(label_name)
        computable = False
        error_msg = ""
        show_error = False
        if error:
            p_val = "Error"
            error_msg = p_txt
            show_error = True
        elif p_txt is None:
            p_val = "not computed"
            computable = True
        else:
            p_val = str(p_txt)
        self.view.update_p_value(p_val, disable_computation=not computable, details=details)
        self.view.update_confounding_warning(error_msg, show_error)

    def compute_multicontest(self):
        current_data = self.data_model.get_merged_data(self.selected_label)
        if current_data is None:
            return
        self.view.enable_label_modification(False)
        self.view.show_progress(True)
        self.current_worker = run_confounding_test(data=current_data,
                                                   cluster_label="cluster",
                                                   factor_label=self.selected_label,
                                                   on_result=self.update_confounding_result,
                                                   on_error=self.confounding_test_failed,
                                                   on_progress=self.view.update_progress)
        self.threadpool.start(self.current_worker)

    def update_confounding_result(self, result: dict):
        if self.current_worker is not None:
            if self.current_worker.is_killed:
                return
        self.test_count += 1
        permutation_p_result = result["permutation_p_value"]
        p_threshold = 1 / result["total_n_iter"]
        if permutation_p_result < p_threshold:
            result["permutation_p_value"] = f"<{p_threshold:.2e}"
        self.data_model.test_results[self.selected_label] = result["permutation_p_value"]
        self.data_model.detailed_results[self.selected_label] = result
        self.view.show_progress(False)
        self.view.update_p_value(result["permutation_p_value"],
                                 disable_computation=True,
                                 details=result)
        self.view.update_test_results(self.data_model.results_table)
        self.view.enable_label_modification(True)

    def confounding_test_failed(self, error: tuple):
        if self.current_worker is not None:
            self.current_worker.kill()
            self.threadpool.clear()
        self.test_count += 1
        error_msg = error[0]
        short_error_msg = error[1]
        label_name = error[2]
        self.data_model.test_errors[label_name] = [error_msg, short_error_msg]
        self.view.show_progress(False)
        self.view.update_p_value("Error", disable_computation=True)
        self.view.show_warning(f"Computation failed for {label_name}!")
        self.view.update_confounding_warning(error_msg, True)
        self.view.update_test_results(self.data_model.results_table)
        self.view.enable_label_modification(True)

    def sort_labels(self, ascending: bool):
        self.data_model.sort_labels(ascending)
        self.update_categories(keep_results=True)

    def reset_results(self):
        self.data_model.clear_results()
        self.test_count = 0
        self.view.update_p_value("not computed", disable_computation=False)

    def clear_all_data(self):
        del self.data_model
        self.data_model = DataModel(self)
        self.test_count = 0
        self.view.clear_view()
