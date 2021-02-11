"""
Interface that any new parser can implement
"""
from datetime import datetime
from typing import Dict
from abc import ABC, abstractmethod
from models.transaction import Transaction
from models.transaction_export import TransactionExport
from utils.helper import save_data_to_json_file


class Parser(ABC):
    def __init__(self, customer_file, vehicle_file=None):
        self.customer_file = customer_file
        self.vehicle_file = vehicle_file

    @abstractmethod
    def extract_customer_data(self):
        pass

    @abstractmethod
    def extract_vehicle_data(self):
        pass

    def generate_json_file_structure(self, customer) -> Dict:
        """
        :param customer: Take customer object
        :return: dictionary of Transaction Export model
        """
        transaction = Transaction(customer)
        return TransactionExport(transaction).to_export()

    def save_data_as_json(self, result) -> None:
        """
        :param result: Dictionary that want to convert to json
        """
        save_data_to_json_file(result, f'output/{datetime.now()}result.json')
