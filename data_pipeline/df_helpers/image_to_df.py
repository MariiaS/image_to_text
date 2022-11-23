import pytesseract
from PIL import Image
from pytesseract import Output


def image_to_text_df(path_to_image):
    text_from_image_df = pytesseract.image_to_data(Image.open(path_to_image), output_type=Output.DATAFRAME)[["text"]]
    return text_from_image_df
