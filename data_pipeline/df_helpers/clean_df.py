import logging

import pandas as pd


def replace_special_chars(df_column):
    chars = "\\`*_{}:[]()>#+-!$"
    if df_column is not None:
        for char in chars:
            df_column = df_column.str.replace(char, '', regex=True)
        return df_column
    else:
        logging.error("input is empty")


def drop_na(df):
    if isinstance(df, pd.DataFrame):
        df_without_nan = df.dropna().reset_index(drop=True)
        return df_without_nan
    else:
        logging.error("not dataframe type")


def column_to_lowercase(df_column):
    if df_column is not None:
        df_column = df_column.str.lower()
        return df_column
    else:
        logging.error("input is incorrect")


def clean_text_df(text_from_image_df):
    text_df = drop_na(text_from_image_df[["text"]])
    text_df["text"] = column_to_lowercase(text_df["text"])
    text_df["text"] = replace_special_chars(text_df["text"])
    return text_df
