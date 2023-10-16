import unittest
import pandas as pd
from multicontest.DataModel import DataModel

class TestDataModel(unittest.TestCase):
    def setUp(self):
        controller = type('controller', (object,), {
            'max_categories': 10,
            'drop_nan_categories': False
        })
        self.data_model = DataModel(controller=controller)
        
        self.data_model.raw_label_data = pd.DataFrame({
            'label1': ['a', 'b', 'c', 'd', 'e'],
            'label2': ['a', 'a', 'b', 'c', 'd'],
            'label3': ['a', 'a', 'b', 'c', 'c'],
            'label4': ['a', 'a', 'a', 'a', 'a'],
            'label5': ['a', 'b', float('NaN'), 'c', float('NaN')],
            'label6': ['a', 'b', float('NaN'), 'c', 'd'],
            'label7': [1, 2, 3, 4, 5],
            'label8': [6, 6, 7, 7, 8],
            'label9': [9, 9, 10, 11, 12],
            'label10': [13, 14, float('NaN'), 15, float('NaN')],
            'label11': [16, float('NaN'), 17, 18, 19],
            'label12': [20, 20, 20, 20, 20],
            'label13': [21, 21, 21, 21, 22],
        }, index=['sample1', 'sample2', 'sample3', 'sample4', 'sample5'])
        
        self.data_model.raw_cls_data = pd.Series(
            [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
            index=['sample1', 'sample2', 'sample3', 'sample4', 'sample5', 'sample6', 'sample7', 'sample8', 'sample9', 'sample10']
        )

        self.label_data = pd.DataFrame({
            'label1': ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e'],
            'label2': ['a', 'a', 'b', 'c', 'd', 'a', 'a', 'b', 'c', 'd'],
            'label3': ['a', 'a', 'b', 'c', 'c', 'a', 'a', 'b', 'c', 'c'],
            'label4': ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            'label5': ['a', 'b', float('NaN'), 'c', float('NaN'), 'a', 'b', float('NaN'), 'c', float('NaN')],
        }, index=['sample1', 'sample2', 'sample3', 'sample4', 'sample5', 'sample6', 'sample7', 'sample8', 'sample9', 'sample10'])

    def test_categorical_labels_with_dropna(self):
        self.data_model.selected_category_threshold = 3
        self.data_model.controller.drop_nan_categories = True
        expected_output = ['label3', 'label5', 'label8', 'label10', 'label13']
        self.assertEqual(self.data_model.categorical_labels, expected_output)

    def test_categorical_labels_without_dropna(self):
        self.data_model.selected_category_threshold = 3
        self.data_model.controller.drop_nan_categories = False
        expected_output = ['label3', 'label8', 'label13']
        self.assertEqual(self.data_model.categorical_labels, expected_output)

    def test_generate_label_count_data_with_dropna(self):
        self.data_model.selected_category_threshold = 3
        self.data_model.controller.drop_nan_categories = True
        self.data_model.generate_label_count_data()
        expected_output = pd.DataFrame({
            'label1': ['a (1)', 'b (1)', 'c (1)', 'd (1)', 'e (1)'],
            'label2': ['a (2)', 'b (1)', 'c (1)', 'd (1)', float('NaN')],
            'label3': ['a (2)', 'c (2)', 'b (1)', float('NaN'), float('NaN')],
            'label4': ['a (5)', float('NaN'), float('NaN'), float('NaN'), float('NaN')],
            'label5': ['a (1)', 'b (1)', 'c (1)', float('NaN'), float('NaN')],
            'label6': ['a (1)', 'b (1)', 'c (1)', 'd (1)', float('NaN')],
            'label7': ['1 (1)', '2 (1)', '3 (1)', '4 (1)', '5 (1)'],
            'label8': ['6 (2)', '7 (2)', '8 (1)', float('NaN'), float('NaN')],
            'label9': ['9 (2)', '10 (1)', '11 (1)', '12 (1)', float('NaN')],
            'label10': ['13.0 (1)', '14.0 (1)', '15.0 (1)', float('NaN'), float('NaN')],
            'label11': ['16.0 (1)', '17.0 (1)', '18.0 (1)', '19.0 (1)', float('NaN')],
            'label12': ['20 (5)', float('NaN'), float('NaN'), float('NaN'), float('NaN')],
            'label13': ['21 (4)', '22 (1)', float('NaN'), float('NaN'), float('NaN')]
        }, index=[0, 1, 2, 3, 4]).T
        pd.testing.assert_frame_equal(self.data_model.label_count_data, expected_output)

    def test_generate_label_count_data_without_dropna(self):
        self.data_model.selected_category_threshold = 3
        self.data_model.controller.drop_nan_categories = False
        self.data_model.generate_label_count_data()
        expected_output = pd.DataFrame({
            'label1': ['a (1)', 'b (1)', 'c (1)', 'd (1)', 'e (1)'],
            'label2': ['a (2)', 'b (1)', 'c (1)', 'd (1)', float('NaN')],
            'label3': ['a (2)', 'c (2)', 'b (1)', float('NaN'), float('NaN')],
            'label4': ['a (5)', float('NaN'), float('NaN'), float('NaN'), float('NaN')],
            'label5': ['nan (2)', 'a (1)', 'b (1)', 'c (1)', float('NaN')],
            'label6': ['a (1)', 'b (1)', 'nan (1)', 'c (1)', 'd (1)'],
            'label7': ['1 (1)', '2 (1)', '3 (1)', '4 (1)', '5 (1)'],
            'label8': ['6 (2)', '7 (2)', '8 (1)', float('NaN'), float('NaN')],
            'label9': ['9 (2)', '10 (1)', '11 (1)', '12 (1)', float('NaN')],
            'label10': ['nan (2)', '13.0 (1)', '14.0 (1)', '15.0 (1)', float('NaN')],
            'label11': ['16.0 (1)', 'nan (1)', '17.0 (1)', '18.0 (1)', '19.0 (1)'],
            'label12': ['20 (5)', float('NaN'), float('NaN'), float('NaN'), float('NaN')],
            'label13': ['21 (4)', '22 (1)', float('NaN'), float('NaN'), float('NaN')]
        }, index=[0, 1, 2, 3, 4]).T
        pd.testing.assert_frame_equal(self.data_model.label_count_data, expected_output)

    def test_reduced_label_count_data_with_dropna(self):
        self.data_model.selected_category_threshold = 3
        self.data_model.controller.drop_nan_categories = True
        self.data_model.generate_label_count_data()
        expected_output = pd.DataFrame({
            'label3': ['a (2)', 'c (2)', 'b (1)'],
            'label5': ['a (1)', 'b (1)', 'c (1)'],
            'label8': ['6 (2)', '7 (2)', '8 (1)'],
            'label10': ['13.0 (1)', '14.0 (1)', '15.0 (1)'],
            'label13': ['21 (4)', '22 (1)', float('NaN')]
        }, index=['category 1', 'category 2', 'category 3']).T
        pd.testing.assert_frame_equal(self.data_model.reduced_label_count_data, expected_output)

    def test_reduced_label_count_data_without_dropna(self):
        self.data_model.selected_category_threshold = 3
        self.data_model.controller.drop_nan_categories = False
        self.data_model.generate_label_count_data()
        expected_output = pd.DataFrame({
            'label3': ['a (2)', 'c (2)', 'b (1)'],
            'label8': ['6 (2)', '7 (2)', '8 (1)'],
            'label13': ['21 (4)', '22 (1)', float('NaN')]
        }, index=['category 1', 'category 2', 'category 3']).T
        pd.testing.assert_frame_equal(self.data_model.reduced_label_count_data, expected_output)

    def test_set_and_validate_clustering_with_series(self):
        cls_data = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
        expected_output = (5, 5)
        self.assertEqual(self.data_model.set_and_validate_clustering(cls_data), expected_output)

    def test_set_and_validate_clustering_with_dataframe(self):
        cls_data = pd.DataFrame({'cluster': [1, 2, 3, 4, 5]}, index=['a', 'b', 'c', 'd', 'e'])
        expected_output = (5, 5)
        self.assertEqual(self.data_model.set_and_validate_clustering(cls_data), expected_output)

    def test_set_and_validate_clustering_with_invalid_data(self):
        cls_data = pd.DataFrame({'cluster': [1, 2, 3, 4, 5], 'other': [1, 2, 3, 4, 5]}, index=['a', 'b', 'c', 'd', 'e'])
        with self.assertRaises(ValueError):
            self.data_model.set_and_validate_clustering(cls_data)

    def test_set_and_validate_clustering_with_nonunique_index(self):
        cls_data = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'a'])
        with self.assertRaises(ValueError):
            self.data_model.set_and_validate_clustering(cls_data)

    def test_set_and_validate_clustering_with_single_cluster(self):
        cls_data = pd.Series([1, 1, 1, 1, 1], index=['a', 'b', 'c', 'd', 'e'])
        with self.assertRaises(ValueError):
            self.data_model.set_and_validate_clustering(cls_data)

    def test_set_and_validate_labels_with_series(self):
        label_data = pd.Series(
            ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e'],
            index=['sample1', 'sample2', 'sample3', 'sample4', 'sample5', 'sample6', 'sample7', 'sample8', 'sample9', 'sample10']
        )
        label_data_df = pd.DataFrame({
            0: ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e'],
        }, index=['sample1', 'sample2', 'sample3', 'sample4', 'sample5', 'sample6', 'sample7', 'sample8', 'sample9', 'sample10'])
        self.data_model.set_and_validate_labels(label_data)
        pd.testing.assert_frame_equal(self.data_model.raw_label_data, label_data_df)

    def test_set_and_validate_labels_with_invalid_data(self):
        label_data = ['a', 'b', 'c', 'd', 'e']
        with self.assertRaises(ValueError):
            self.data_model.set_and_validate_labels(label_data)

    def test_set_and_validate_labels_with_insufficient_samples(self):
        label_data = pd.DataFrame({
            'label1': ['a', 'b', 'c', 'd'],
            'label2': ['a', 'a', 'b', 'c'],
            'label3': ['a', 'a', 'b', 'c'],
            'label4': ['a', 'a', 'a', 'a'],
            'label5': ['a', 'b', float('NaN'), 'c'],
            'label6': ['a', 'b', float('NaN'), 'c'],
            'label7': [1, 2, 3, 4],
            'label8': [6, 6, 7, 7],
            'label9': [9, 9, 10, 11],
            'label10': [13, 14, float('NaN'), 15],
            'label11': [16, float('NaN'), 17, 18],
            'label12': [20, 20, 20, 20],
            'label13': [21, 21, 21, 21],
        }, index=[1, 2, 3, 4])
        with self.assertRaises(ValueError):
            self.data_model.set_and_validate_labels(label_data)

    def test_set_and_validate_labels_with_valid_data(self):
        self.data_model.set_and_validate_labels(self.label_data)
        pd.testing.assert_frame_equal(self.data_model.raw_label_data, self.label_data)

if __name__ == '__main__':
    unittest.main()
