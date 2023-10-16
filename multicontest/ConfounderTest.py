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

__author__ = "Nicolas Kersten and Markus Wallner"
__license__ = 'GNU General Public License v3.0'

import sys
import traceback

import numpy as np
import pandas as pd
from PySide6.QtCore import QObject, QRunnable, Signal, Slot
from numpy.random import MT19937, default_rng
from scipy import stats
from scipy.stats import binomtest


def run_chi2_test(factor_data: np.array, cluster_data: np.array) -> tuple[float, np.ndarray]:
    """ Perform chi-squared test for confounding
    :param factor_data: numpy array containing the factor data
    :param cluster_data: numpy array containing the cluster data
    :return: p-value and expected values
    """
    cont_tbl = pd.crosstab(factor_data, cluster_data)
    chi2, p, dof, ex = stats.chi2_contingency(cont_tbl)
    return p, ex


def check_chi2_expected_values(expected: np.ndarray) -> bool:
    """ Check if the expected values for the chi-squared test meet the conditions
    :param expected: numpy array containing the expected values
    :return: boolean indicating if the conditions are met
    """
    exp_smaller_one = sum(list((expected < 1).flat))
    exp_smaller_five = sum(list((expected < 5).flat))
    fraction_smaller_five = (exp_smaller_five / expected.size)

    return (exp_smaller_one == 0) and (fraction_smaller_five <= 0.2)


def single_permutation_test(clustering: np.ndarray, conf_factor_data: np.ndarray, rng=None) -> tuple[float, int]:
    """ Perform a single permutation test
    :param clustering: numpy array containing the cluster data
    :param conf_factor_data: numpy array containing the factor data
    :param rng: random number generator
    :return: p-value and number of skipped permutations
    """
    current_p = 1  # initialize p-value as a fallback
    valid_permutation_tested = False
    number_tested_permutations = 0
    max_number_tested_permutations = 100

    while (not valid_permutation_tested) and (number_tested_permutations < max_number_tested_permutations):
        # check the number of skipped permutations
        if number_tested_permutations == max_number_tested_permutations:
            break

        # generate permutation
        if rng is None:
            perm_clustering = np.random.choice(clustering, size=clustering.shape[0], replace=False)
        else:
            perm_clustering = rng.choice(clustering, size=clustering.shape[0], replace=False)

        # compute p-value and expected values to check for chi-squared test conditions
        current_p, current_expected_values = run_chi2_test(conf_factor_data, perm_clustering)
        valid_permutation_tested = check_chi2_expected_values(current_expected_values)
        number_tested_permutations += 1

    number_skipped_permutations = number_tested_permutations - 1

    return current_p, number_skipped_permutations


def permutation_confounding_test(data: pd.DataFrame, factor_label: str, cluster_label: str = "cluster",
                                 max_n_iter: int = 1e5, random_seed: int = None, rng=MT19937,
                                 progress_callback: Signal = None, error: Signal = None) -> dict or None:
    """ Perform permutation testing of p-values and compute adjusted p-values using binomial test
    :param data: pandas dataframe containing the data
    :param factor_label: label of the factor to test for confounding
    :param cluster_label: label of the cluster assignment
    :param max_n_iter: maximum number of iterations
    :param random_seed: random seed for reproducibility
    :param rng: random number generator
    :param progress_callback: signal for progress bar
    :param error: signal for error message
    :return: dictionary containing the results of the permutation test or None if the test failed
    """
    single_step = 90 / max_n_iter
    current_progress = 0
    if progress_callback is not None:
        progress_callback.emit(current_progress)
    clustering = data[cluster_label].to_numpy()
    conf_factor_data = data[factor_label].to_numpy()
    rng = default_rng(rng(random_seed))
    original_p_val, original_expected_values = run_chi2_test(conf_factor_data, clustering)
    chi_squared_conditions_met = check_chi2_expected_values(original_expected_values)

    if not chi_squared_conditions_met:
        if error is not None:
            error.emit(("The expected values for the contingency table of the clustering do not "
                        "meet chi-squared test conditions!", "Chi-squared conditions not met!",
                        factor_label))
        return

    cur_p_value = original_p_val
    sig_threshold = 0.05
    n_iter = 1000
    total_n_iter = 0
    total_n_extreme = 0
    total_skipped_permutations = 0
    continue_testing = True
    current_progress += 10

    if progress_callback is not None:
        progress_callback.emit(current_progress)

    while continue_testing:
        perm_p_vals = []
        for i in range(n_iter):
            tmp_p_val, tmp_num_skipped = single_permutation_test(clustering, conf_factor_data, rng=rng)
            perm_p_vals.append(tmp_p_val)
            total_skipped_permutations += tmp_num_skipped
            if total_skipped_permutations > max_n_iter:
                if error is not None:
                    error.emit(("Number of redrawn permutations exceeded maximum allowed number of iterations!",
                                "Too many invalid permutations!",
                                factor_label))
                return
            current_progress += single_step
            if progress_callback is not None:
                progress_callback.emit(current_progress)

        total_n_iter += n_iter
        tmp_n_extreme = np.array(perm_p_vals) <= original_p_val
        total_n_extreme += np.sum(tmp_n_extreme.astype(int))

        binom_res = binomtest(total_n_extreme, total_n_iter, alternative='two-sided')
        cur_p_value = binom_res.proportion_estimate
        cur_conf_int = binom_res.proportion_ci()

        threshold_in_conf = (cur_conf_int[0] < sig_threshold) and (cur_conf_int[1] > sig_threshold)
        if (not threshold_in_conf) or (total_n_iter >= max_n_iter):
            continue_testing = False

    permutation_test_results = {'permutation_p_value': cur_p_value, 'original_p_value': original_p_val,
                                'total_n_iter': total_n_iter, 'total_n_skipped': total_skipped_permutations}
    if progress_callback is not None:
        progress_callback.emit(100)
    return permutation_test_results


class Worker(QRunnable):

    def __init__(self, function, *args, **kwargs):
        super().__init__()
        self.is_killed = False
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        self.kwargs["progress_callback"] = self.signals.progress
        self.kwargs["error"] = self.signals.error

    @Slot()
    def run(self):

        # Retrieve args/kwargs and use them to start processing
        try:
            result = self.function(*self.args, **self.kwargs)
        except:  # broad exception to catch all errors that might occur in the function
            exception_type, value = sys.exc_info()[:2]
            self.signals.error.emit((exception_type, value, traceback.format_exc()))
            self.kill()
        else:
            self.signals.result.emit(result)  # Return the result of the processing

    def kill(self):
        self.is_killed = True


class WorkerSignals(QObject):
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)


def run_confounding_test(data: pd.DataFrame, factor_label: str, cluster_label: str,
                         on_result: callable, on_error: callable, on_progress: callable) -> Worker:
    """ Run the confounding test in a separate thread
    :param data: pandas dataframe containing the data
    :param factor_label: label of the factor to test for confounding
    :param cluster_label: label of the cluster assignment
    :param on_result: callback function for the result
    :param on_error: callback function for the error
    :param on_progress: callback function for the progress
    :return: Worker
    """
    multicontest_worker = Worker(permutation_confounding_test, data=data, factor_label=factor_label,
                                 cluster_label=cluster_label)
    multicontest_worker.signals.result.connect(on_result)
    multicontest_worker.signals.error.connect(on_error)
    multicontest_worker.signals.progress.connect(on_progress)
    return multicontest_worker
