"""
class to parse csv file
"""
from typing import List
from .parser import Parser
from utils.helper import get_data_from_csv_file
from resource.parser_exception import ParserException


class CsvParser(Parser):
    def __init__(self, customer_file, vehicle_file):
        Parser.__init__(self, customer_file, vehicle_file)

    def extract_customer_data(self) -> List:
        try:
            customer_data = get_data_from_csv_file(self.customer_file)

            customers = [
                {
                    "_id": line[0],
                    "name": line[1],
                    "address": line[2],
                    "phone": line[3],
                    "date": line[4]
                }
                for line in customer_data
            ]
            return customers
        except Exception as e:
            raise ParserException('error in parse customer file')

    def extract_vehicle_data(self) -> List:
        try:
            vehicle_data = get_data_from_csv_file(self.vehicle_file)
            vehicles = [
                {
                    "_id": line[0],
                    "make": line[1],
                    "vin_number": line[2],
                    "owner_id": line[3]
                }
                for line in vehicle_data
            ]
            return vehicles
        except Exception as e:
            raise ParserException('error in parse vehicle file')

