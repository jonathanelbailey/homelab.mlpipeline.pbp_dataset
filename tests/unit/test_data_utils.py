import unittest
import pandas as pd
from unittest.mock import patch
from src.data_utils import load_pbp_data, clean_nfl_data, save_to_csv

class TestDataUtils(unittest.TestCase):

    def setUp(self):
        self.test_data = pd.DataFrame({
            'column1': [1, 2, 3],
            'column2': ['a', 'b', 'c']
        })
        self.seasons = [2019, 2020]

    @patch('src.data_utils.nfl.import_pbp_data')
    def test_load_pbp_data(self, mock_import_pbp_data):
        mock_import_pbp_data.return_value = self.test_data
        result = load_pbp_data(self.seasons)
        mock_import_pbp_data.assert_called_with(self.seasons, thread_requests=True)
        pd.testing.assert_frame_equal(result, self.test_data)

    @patch('src.data_utils.nfl.clean_nfl_data')
    def test_clean_nfl_data(self, mock_clean_nfl_data):
        mock_clean_nfl_data.return_value = self.test_data
        result = clean_nfl_data(self.test_data)
        mock_clean_nfl_data.assert_called_with(self.test_data)
        pd.testing.assert_frame_equal(result, self.test_data)

    @patch("pandas.DataFrame.to_csv")
    def test_save_to_csv(self, mock_to_csv):
        file_prefix = 'dummy_prefix'
        season = self.seasons[0]
        df_tuple = (self.seasons[0], file_prefix, self.test_data)
        expected_filename = f'{file_prefix}_{season}.csv'
        save_to_csv(df_tuple)
        mock_to_csv.assert_called_with(expected_filename)


if __name__ == '__main__':
    unittest.main()