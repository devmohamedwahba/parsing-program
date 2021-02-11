"""
class to represent final structure of file
"""
from typing import Dict
from utils.helper import get_file_name


class TransactionExport:
    def __init__(self, transaction):
        self.transaction = transaction

    def to_export(self) -> Dict:
        """
        :return: Dictionary representation of file
        """
        return {
            "file_name": get_file_name(),
            "transaction": self.transaction.to_json()
        }
