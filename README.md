# Image to text

The main focus of the repository to take image files with floor plans as an input, read the total area of the plan and output in csv file total area in feet and metres for each image 
Logs on info level are enabled to follow the steps of the program.

## Architecture
Main application is in the _data_pipeline_ folder.
Input images are stored in `images` folder
Tests are stored in `data_pipeline/tests`
Program is executed in file `data_pipeline/main.py`
Output is stored in `csv_files/total_area.csv`

Main principles followed: 
1. Clean code - code should speak for itself
2. KISS - simple and clear code
3. PEP8 
4. Functional programming - create pure functions whenever possible

## Installation

for Mac: 
   `brew instal tesseract`

## Execution
Through IDE: 
     ` execute data_pipeline/main.py`
constants `DIR_PATH` and `FILE_PATH` are introduced in the same file

