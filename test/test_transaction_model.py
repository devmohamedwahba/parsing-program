import unittest
from models.customer import Customer
from models.vehicle import Vehicle
from models.transaction import Transaction


class TestTransaction(unittest.TestCase):
    def setUp(self) -> None:
        self.customer_data = {
            "_id": "123",
            "name": "Test Customer",
            "address": "Cairo",
            "phone": "0123456789",
            "date": "13-2-2021",
        }
        self.vehicle_data = {
            "_id": "123",
            "make": "Test Vehicle",
            "vin_number": "5555",
            "owner_id": "0123456789",
        }
        self.customer = Customer(**self.customer_data)
        self.vehicle = Vehicle(**self.vehicle_data)

    def test_transaction_to_json(self):
        expected = {
            "date": "13-2-2021",
            "customer": {
                "id": "123",
                "name": "Test Customer",
                "address": "Cairo",
                "phone": "0123456789",
            },
            "vehicle": [
                {
                    "id": "123",
                    "make": "Test Vehicle",
                    "vin_number": "5555",
                }
            ]
        }
        result = {
            "date": self.customer.date,
            "customer": self.customer.to_json(),
            "vehicle": [
                self.vehicle.to_json()
            ]
        }

        self.assertDictEqual(result, expected)
