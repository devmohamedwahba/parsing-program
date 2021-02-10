"""
main concern is to have some helper function to help in  extract and save data
"""
import json


def get_data_from_csv_file(file_name):
    with open(file_name, 'r') as file:
        lines = [[element[1:-1] for element in line.strip().split(',')] for line in file.readlines()]
    return lines[1:]


def save_data_to_json_file(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2)
