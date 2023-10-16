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

import pandas as pd


class DataModel:

    def __init__(self, controller):
        self.controller = controller
        self.raw_cls_data = pd.Series(dtype=str)
        self.raw_label_data = pd.DataFrame()
        self.label_count_data = pd.DataFrame()
        self.selected_category_threshold = 10
        self.test_results = {}  # key: label name, value: confounding test result
        self.detailed_results = {}  # key: label name, value: detailed test result
        self.test_errors = {}  # key: label name, value: error message

    @property
    def dropna(self) -> bool:
        return self.controller.drop_nan_categories

    @property
    def preview_cls_data(self) -> pd.DataFrame:
        if not self.raw_cls_data.empty:
            return self.raw_cls_data.to_frame()
        else:
            return pd.DataFrame()

    @property
    def unique_cls_data(self) -> pd.DataFrame:
        if not self.raw_cls_data.empty:
            tmp = self.raw_cls_data.value_counts(dropna=False).to_frame()
            tmp.columns = ['count']
            tmp.index.name = 'cluster'
            return tmp
        else:
            return pd.DataFrame()

    @property
    def all_label_names(self) -> list:
        return list(self.raw_label_data.columns)

    @property
    def categorical_labels(self) -> list:
        min_cat = 2
        cat_labels = []
        for label in self.raw_label_data.columns:
            tmp_unique = self.raw_label_data[label].unique()
            if self.dropna:
                tmp_unique = tmp_unique[~pd.isnull(tmp_unique)]
            if min_cat <= len(tmp_unique) <= self.selected_category_threshold:
                cat_labels.append(label)
        return cat_labels

    @property
    def reduced_label_data(self) -> pd.DataFrame:
        return self.raw_label_data[self.categorical_labels]

    @property
    def reduced_label_count_data(self) -> pd.DataFrame:
        tmp = self.label_count_data.loc[self.categorical_labels].dropna(axis=1, how='all')
        new_cols = [f"category {i + 1}" for i in range(tmp.shape[1])]
        tmp.columns = new_cols
        return tmp

    @property
    def total_sample_count(self) -> int:
        return self.raw_cls_data.shape[0]

    @property
    def sample_overlap(self) -> int:
        return len(set(self.raw_label_data.index).intersection(set(self.raw_cls_data.index)))

    @property
    def total_label_count(self) -> int:
        return self.raw_label_data.shape[1]

    @property
    def reduced_label_count(self) -> int:
        return self.reduced_label_data.shape[1]

    @property
    def results_table(self) -> pd.DataFrame:
        if self.detailed_results:
            tmp = pd.DataFrame(self.detailed_results).T
            tmp["redrawn permutations [%]"] = tmp["total_n_skipped"] / tmp["total_n_iter"] * 100
            tmp.rename(columns={"original_p_value": "original p-value", "permutation_p_value": "permutation p-value",
                                "total_n_iter": "# iterations", "total_n_skipped": "# skipped iterations"},
                       inplace=True)
            tmp = tmp[["permutation p-value", "original p-value", "redrawn permutations [%]"]]
            tmp_errors = pd.DataFrame(self.test_errors, index=["detailed error", "error"]).T
            tmp_errors.drop("detailed error", axis=1, inplace=True)
            tmp = pd.concat([tmp, tmp_errors], axis=1, join="outer")
            return tmp.dropna(axis=1, how="all")
        elif self.test_errors:
            tmp_errors = pd.DataFrame(self.test_errors, index=["detailed error", "error"]).T
            tmp_errors.drop("detailed error", axis=1, inplace=True)
            return tmp_errors
        else:
            return pd.DataFrame()

    def set_and_validate_clustering(self, cls_data) -> tuple[int, int]:
        if not isinstance(cls_data, pd.Series):
            if isinstance(cls_data, pd.DataFrame) and cls_data.shape[1] == 1:
                cls_data = cls_data.iloc[:, 0]
            else:
                raise ValueError("Clustering data may only contain one column with cluster labels.")
        cls_data.name = 'cluster'
        cls_data.index = cls_data.index.astype(str)
        if not cls_data.index.is_unique:
            raise ValueError("Clustering data must have unique index values (sample names).")
        cluster_count = len(cls_data.unique())
        if cluster_count < 2:
            raise ValueError("Clustering data must have at least two clusters.")
        self.raw_cls_data = cls_data
        sample_count = len(cls_data)
        return cluster_count, sample_count

    def set_and_validate_labels(self, label_data: pd.Series or pd.DataFrame):
        if isinstance(label_data, pd.Series):
            label_data = label_data.to_frame()
        if not isinstance(label_data, pd.DataFrame):
            raise ValueError("")  # internal error -> no message to user
        label_data.index = label_data.index.astype(str)
        min_sample_count = 5 * self.raw_cls_data.nunique()
        if len(set(label_data.index).intersection(set(self.raw_cls_data.index))) < min_sample_count:
            raise ValueError(f"Label data must have a sufficient number of samples in common with clustering data.\n"
                             f"Minimum number of samples: {min_sample_count} (5 * number of clusters)")
        self.raw_label_data = label_data
        self.generate_label_count_data()

    def generate_label_count_data(self):
        tmp_df = pd.DataFrame()
        for label in self.raw_label_data.columns:
            tmp = self.raw_label_data[label].value_counts(dropna=self.dropna).to_frame().reset_index()
            tmp.columns = ["name", 'count']
            tmp[label] = tmp["name"].astype(str) + " (" + tmp["count"].astype(str) + ")"
            tmp.drop(columns=['name', 'count'], inplace=True)
            tmp_df = tmp_df.merge(tmp, left_index=True, right_index=True, how='outer')
        self.label_count_data = tmp_df.T

    def is_valid_label(self, label) -> bool:
        return label in self.all_label_names

    def get_overlap(self, current_label: str) -> tuple[list, int]:
        if not self.is_valid_label(current_label):
            return [], 0
        label_data = self.raw_label_data[current_label]
        if self.dropna:
            label_data = label_data.dropna(how='any')
        overlap = list(set(label_data.index).intersection(set(self.raw_cls_data.index)))
        if self.dropna:
            missing_count = 0
        else:
            missing_count = self.raw_label_data.loc[overlap, current_label].isna().sum()
        return overlap, missing_count

    def get_merged_data(self, current_label: str) -> pd.DataFrame or None:
        if not self.is_valid_label(current_label):
            return None
        merged_data = self.raw_label_data[current_label].to_frame().merge(self.raw_cls_data.to_frame(),
                                                                          left_index=True, right_index=True)
        if self.dropna:
            merged_data.dropna(how='any', inplace=True)
        else:
            overlap, _ = self.get_overlap(current_label)
            merged_data = merged_data.loc[overlap]
            merged_data.fillna("nan", inplace=True)
        return merged_data

    def get_vis_data(self, current_label: str) -> tuple[dict, list] or tuple[None, None]:
        if not self.is_valid_label(current_label):
            return None, None
        merged_data = self.get_merged_data(current_label)
        vis_df = pd.crosstab(merged_data[current_label], merged_data['cluster'])
        vis_df = vis_df / vis_df.sum(axis=0) * 100
        vis_dict = {}
        for idx in vis_df.index:
            row = vis_df.loc[idx]
            vis_dict[idx] = ([str(x) for x in row.index], row.to_numpy())
        x_ticks = [str(x) for x in vis_df.columns]
        return vis_dict, x_ticks

    def get_contingency_table(self, current_label: str) -> pd.DataFrame:
        if not self.is_valid_label(current_label):
            return pd.DataFrame()
        merged_data = self.get_merged_data(current_label)
        cont_tbl = pd.crosstab(merged_data[current_label], merged_data['cluster'])
        return cont_tbl

    def get_p_value(self, current_label: str) -> tuple[float, bool] or tuple[None, bool]:
        if current_label in self.test_results:
            return self.test_results[current_label], False
        if current_label in self.test_errors:
            return self.test_errors[current_label][0], True
        return None, False

    def get_detailed_results(self, current_label: str) -> dict or None:
        if current_label in self.detailed_results:
            return self.detailed_results[current_label]
        return None

    def get_current_result_table(self, current_label: str) -> pd.DataFrame or None:
        if not self.is_valid_label(current_label):
            return None
        if current_label in self.detailed_results:
            tmp = pd.DataFrame(self.detailed_results[current_label], index=[current_label])
            tmp["redrawn permutations [%]"] = tmp["total_n_skipped"] / tmp["total_n_iter"] * 100
            tmp.rename(columns={"original_p_value": "original p-value", "permutation_p_value": "permutation p-value",
                                "total_n_iter": "# iterations", "total_n_skipped": "# skipped iterations"},
                       inplace=True)
            tmp = tmp[["permutation p-value", "original p-value", "redrawn permutations [%]"]]
            tmp.reset_index(inplace=True, names=["potential confounding factor"])
            return tmp.T
        return None

    def sort_labels(self, ascending: bool = True):
        self.raw_label_data.sort_index(axis=1, inplace=True, ascending=ascending)

    def clear_results(self):
        self.test_results = {}
        self.test_errors = {}
        self.detailed_results = {}
