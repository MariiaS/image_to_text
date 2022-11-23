import logging
import re

import pandas as pd

from text_vars import number_regex


def df_with_total_area(text_df, total_labels):
    total_index = 0
    if isinstance(text_df, pd.DataFrame) & (total_labels != []) & (text_df is not None):
        for total_label in total_labels:
            if text_df['text'].str.startswith(total_label).any():
                total_index = text_df.index[text_df['text'].str.contains(total_label)].tolist()[0]
            break
        total_df = text_df[total_index:total_index + 10].reset_index(drop=True)
        return total_df
    else:
        logging.error("input df is incorrect")


def find_area(total_df, labels):
    area = 0
    if isinstance(total_df, pd.DataFrame) & (labels != []) & (total_df is not None):
        for index in range(len(total_df)-1, 0, -1):
            if any(map(total_df.loc[index]["text"].__contains__, labels)):
                for float_index in range(index, index - 3, -1):
                    if re.match(number_regex, total_df.loc[float_index]["text"]):
                        area = re.findall(number_regex, total_df.loc[float_index]["text"])[0]
                        break
        return area
    else:
        logging.error("input df is incorrect")

