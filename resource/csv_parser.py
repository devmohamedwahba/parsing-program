from .parser import Parser
from utils.helper import get_data_from_csv_file


class CsvParser(Parser):
    def __init__(self, customer_file, vehicle_file):
        Parser.__init__(self, customer_file, vehicle_file)

    def extract_customer_data(self):
        return get_data_from_csv_file(self.customer_file)

    def extract_vehicle_data(self):
        return get_data_from_csv_file(self.vehicle_file)
