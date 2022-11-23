from unittest import TestCase

import pandas as pd

from df_helpers.clean_df import replace_special_chars, drop_na, column_to_lowercase


class Test(TestCase):
    def test_replace_special_chars(self):
        test_data = ["(124,-5hi", "12.{5:)}"]
        df = pd.DataFrame(test_data, columns=['text'])
        actual_result = replace_special_chars(df['text']).tolist()
        self.assertEqual(actual_result, ["124,5hi", "12.5"])

    def test_replace_special_chars_none_input(self):
        self.assertRaises(TypeError, replace_special_chars(None))

    def test_drop_na(self):
        test_data = ["124,5", None, "total", "", None]
        df = pd.DataFrame(test_data, columns=['text'])
        actual_result = drop_na(df)['text'].tolist()
        self.assertEqual(actual_result, ["124,5", "total", ""])

    def test_drop_na_none(self):
        self.assertEqual(drop_na(None), None)
        self.assertEqual(drop_na([""]), None)

    def test_column_to_lowercase(self):
        test_data = ["Total", "Approx M"]
        df = pd.DataFrame(test_data, columns=['text'])
        actual_result = column_to_lowercase(df['text']).tolist()
        self.assertEqual(actual_result, ["total", "approx m"])
        self.assertNotEqual(actual_result, ["total", "approx M"])
