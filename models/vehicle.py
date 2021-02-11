"""
class to represent Vehicle structure
"""
from typing import Dict


class Vehicle:
    def __init__(self, _id, make, vin_number, owner_id=None):
        self.id = _id
        self.make = make
        self.vin_number = vin_number
        self.owner_id = owner_id

    def to_json(self) -> Dict:
        """
        :return:  Dictionary representation of Vehicle
        """
        return {
            "id": self.id,
            "make": self.make,
            "vin_number": self.vin_number,
        }
