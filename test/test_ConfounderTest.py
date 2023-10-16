import unittest
import numpy as np

from multicontest.ConfounderTest import run_chi2_test, check_chi2_expected_values, single_permutation_test


class TestConfounderTest(unittest.TestCase):

    def test_run_chi2_test(self):
        # Test case 1: Test with valid input
        factor_data = np.array([1, 2, 3, 4, 5])
        cluster_data = np.array([1, 1, 2, 2, 2])
        p, ex = run_chi2_test(factor_data, cluster_data)
        self.assertIsInstance(p, float)
        self.assertIsInstance(ex, np.ndarray)

        # Test case 2: Test with invalid input
        factor_data = np.array([1, 2, 3, 4, 5])
        cluster_data = np.array([1, 1, 2, 2])
        with self.assertRaises(ValueError):
            p, ex = run_chi2_test(factor_data, cluster_data)

        # Test case 3: Test with empty input
        factor_data = np.array([])
        cluster_data = np.array([])
        with self.assertRaises(ValueError):
            p, ex = run_chi2_test(factor_data, cluster_data)

        # Test case 4: Test with large input
        factor_data = np.random.randint(0, 100, size=(1000,))
        cluster_data = np.random.randint(0, 100, size=(1000,))
        p, ex = run_chi2_test(factor_data, cluster_data)
        self.assertIsInstance(p, float)
        self.assertIsInstance(ex, np.ndarray)

        # Test case 5: Test correct output, not significant
        factor_data = np.array([1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2])
        cluster_data = np.array([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2])
        p, ex = run_chi2_test(factor_data, cluster_data)
        self.assertGreater(p, 0.05)
        self.assertTrue(np.allclose(ex, np.array([[3.0, 3.0], [3.0, 3.0]])))

        # Test case 6: Test correct output, significant
        factor_data = np.array([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
        cluster_data = np.array([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2])
        p, ex = run_chi2_test(factor_data, cluster_data)
        self.assertLess(p, 0.05)
        self.assertTrue(np.allclose(ex, np.array([[2.5, 2.5], [3.5, 3.5]])))

        # Test case 7: Test correct output, significant, non-numerical data
        factor_data = np.array(["a", "a", "a", "a", "a", "a", "a", "b", "b", "b", "b", "b"])
        cluster_data = np.array(["a", "a", "a", "a", "a", "a", "b", "b", "b", "b", "b", "b"])
        p, ex = run_chi2_test(factor_data, cluster_data)
        self.assertLess(p, 0.05)
        self.assertTrue(np.allclose(ex, np.array([[3.5, 3.5], [2.5, 2.5]])))

    def test_check_chi2_expected_values(self):
        # Test case 1: Test with valid input
        expected = np.array([[10, 20], [30, 40]])
        self.assertTrue(check_chi2_expected_values(expected))

        # Test case 2: Test with invalid input
        expected = np.array([[0, 0], [0, 0]])
        self.assertFalse(check_chi2_expected_values(expected))

        # Test case 3: Test with invalid input
        expected = np.array([[1, 2], [3, 4]])
        self.assertFalse(check_chi2_expected_values(expected))

        # Test case 4: Test with invalid input
        expected = np.array([[1, 1], [1, 1]])
        self.assertFalse(check_chi2_expected_values(expected))

        # Test case 5: Test with valid input
        expected = np.array([[5, 5], [5, 5]])
        self.assertTrue(check_chi2_expected_values(expected))

        # Test case 6: Test with valid input
        expected = np.array([[5, 7, 6], [6, 8, 4]])
        self.assertTrue(check_chi2_expected_values(expected))

    def test_single_permutation_test(self):
        """ Only test the function signature and return types, not the actual functionality due to randomness"""
        # Test case 1: Test with valid input
        clustering = np.array([1, 1, 2, 2, 2])
        conf_factor_data = np.array([1, 2, 3, 4, 5])
        p, skipped = single_permutation_test(clustering, conf_factor_data)
        self.assertIsInstance(p, float)
        self.assertIsInstance(skipped, int)

        # Test case 2: Test with invalid input
        clustering = np.array([1, 1, 2, 2])
        conf_factor_data = np.array([1, 2, 3, 4, 5])
        with self.assertRaises(ValueError):
            p, skipped = single_permutation_test(clustering, conf_factor_data)

        # Test case 3: Test with empty input
        clustering = np.array([])
        conf_factor_data = np.array([])
        with self.assertRaises(ValueError):
            p, skipped = single_permutation_test(clustering, conf_factor_data)

        # Test case 4: Test with large input
        clustering = np.random.randint(0, 100, size=(1000,))
        conf_factor_data = np.random.randint(0, 100, size=(1000,))
        p, skipped = single_permutation_test(clustering, conf_factor_data)
        self.assertIsInstance(p, float)
        self.assertIsInstance(skipped, int)


if __name__ == '__main__':
    unittest.main()
