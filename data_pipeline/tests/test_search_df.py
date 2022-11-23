from unittest import TestCase

import pandas as pd

from df_helpers.clean_df import drop_na, column_to_lowercase
from df_helpers.search_df import df_with_total_area, find_area


class Test(TestCase):
    def test_df_with_total_area(self):
        test_data = ["", "18276.4", "total", "hi", "10m"]
        df = pd.DataFrame(test_data, columns=['text'])
        actual_result = df_with_total_area(df, ['total'])['text'].tolist()
        self.assertEqual(actual_result, ['total', 'hi', '10m'])

    def test_df_with_total_area_none(self):
        test_data = ["", "18276.4", "total", "hi", "10m"]
        df = pd.DataFrame(test_data, columns=['text'])
        self.assertEqual(df_with_total_area(None, ["total"]), None)
        self.assertEqual(df_with_total_area(df, []), None)

    def test_find_area(self):
        test_data = ["total", "hi", "10", "55", "ft"]
        df = pd.DataFrame(test_data, columns=['text'])
        actual_result = find_area(df, ['ft'])
        self.assertEqual(actual_result, "55")

    def test_find_area_none(self):
        test_data = ["", "18276.4", "total", "hi", "10m"]
        df = pd.DataFrame(test_data, columns=['text'])
        self.assertEqual(find_area(None, ["ft"]), None)
        self.assertEqual(find_area(df, []), None)
