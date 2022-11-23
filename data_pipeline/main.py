import logging

from df_helpers.clean_df import clean_text_df
from df_helpers.image_to_df import image_to_text_df
from df_helpers.search_df import df_with_total_area, find_area
from file_helpers.read_from_dir import files_in_dir
from file_helpers.write_to_csv import write_to_file
from text_vars import alternative_total_labels, feet_labels, meter_labels

DIR_PATH = "images"
FILE_PATH = "csv_files/total_area.csv"

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    logging.info("Reading files from the directory")
    for filename in files_in_dir(DIR_PATH):
        logging.info("Reading text from image " + filename)
        df = image_to_text_df(filename)
        logging.info("Cleaning text data")
        df = clean_text_df(df)
        logging.info("Finding total area records")
        total_df = df_with_total_area(df, alternative_total_labels)
        area_meters = find_area(total_df, meter_labels)
        area_feet = find_area(total_df, feet_labels)
        row = [filename, area_meters, "sq.m.", area_feet, "sq.ft."]
        logging.info("Writing to the csv file")
        write_to_file(FILE_PATH, row)
