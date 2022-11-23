import os

from text_vars import image_extensions


def files_in_dir(dir_path):
    files = []
    for file in os.listdir(dir_path):
        if file.endswith(tuple(image_extensions)):
            files.append(dir_path + "/" + file)
    files.reverse()
    return files
