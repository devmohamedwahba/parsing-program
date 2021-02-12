"""
main concern is to have some helper function to help in  extract and save data
"""
import json
from typing import List
from utils.arguments import Arguments


def get_data_from_csv_file(file_name) -> List[List]:
    """
    :param file_name:  file name to read
    :return: list of lists that can take from csv file
    """
    with open(file_name, 'r') as file:
        lines = [
            [element[1:-1] for element in line.strip().split(',')]
            for line in file.readlines()
        ]
    return lines[1:]


def save_data_to_json_file(data, file_name) -> None:
    """
    :param data: dictionary you want to convert to json
    :param file_name: file path that you want to save json to
    """
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2)


def read_xml_file(file_name) -> str:
    """
    :param file_name: xml file you want to read
    :return: string of xml file
    """
    with open(file_name, 'r') as file:
        return file.read()


def get_file_name() -> str:
    """
    :return: generate file name from file format + file path
    """
    file_format = Arguments.get_format_of_file()
    customer_file_name = Arguments.get_first_file_name()
    return f'{file_format}/{customer_file_name}'
