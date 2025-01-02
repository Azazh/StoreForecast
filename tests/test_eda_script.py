import unittest
from unittest.mock import patch
import pandas as pd
import numpy as np
from src.eda_script import load_data, merge_data, handle_missing_values


class TestEDAScript(unittest.TestCase):

    @patch('src.eda_script.pd.read_csv')  # Mock read_csv
    def test_load_data(self, mock_read_csv):
        # Mock CSV data
        mock_read_csv.side_effect = [
            pd.DataFrame({'Store': [1, 2], 'Sales': [100, 200]}),  # train
            pd.DataFrame({'Store': [1, 2]}),                      # test
            pd.DataFrame({'Store': [1, 2], 'CompetitionDistance': [500, 1000]}),  # store
        ]

        train, test, store = load_data()

        # Assertions
        self.assertEqual(len(train), 2)
        self.assertEqual(len(test), 2)
        self.assertEqual(len(store), 2)

    def test_merge_data(self):
        # Mock data
        train = pd.DataFrame({'Store': [1, 2], 'Sales': [100, 200]})
        test = pd.DataFrame({'Store': [1, 2]})
        store = pd.DataFrame({'Store': [1, 2], 'CompetitionDistance': [500, 1000]})

        train_merged, test_merged = merge_data(train, test, store)

        # Assertions
        self.assertIn('CompetitionDistance', train_merged.columns)
        self.assertIn('CompetitionDistance', test_merged.columns)
        self.assertEqual(train_merged['CompetitionDistance'].tolist(), [500, 1000])

    def test_handle_missing_values(self):
        train = pd.DataFrame({'CompetitionDistance': [np.nan, 1000]})
        handle_missing_values(train)

        # Assertions
        self.assertFalse(train['CompetitionDistance'].isnull().any())
        self.assertEqual(train['CompetitionDistance'][0], 1000)


if __name__ == '__main__':
    unittest.main()
