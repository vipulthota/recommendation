from pathlib import Path
import json


directory = Path(r"D:\dell_hackathon\BuyFair\DFF\mysite\user_inputs")

json_files = list(directory.glob("user-data(*).json"))

if json_files:
    # Sort the JSON files by their numbers (as integers)
    json_files.sort(key=lambda file: int(file.stem.replace("user-data(", "").replace(")", "")))

    # Get the file with the highest number
    highest_number_json = json_files[-1]

    # Open and read the JSON file
    with open(highest_number_json, "r") as file:
        data = json.load(file)
    
    # Now 'data' contains the contents of the JSON file with the highest number
    print(data)