import unittest
from models.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self) -> None:
        self.data = {
            "_id": "123",
            "name": "Test Customer",
            "address": "Cairo",
            "phone": "0123456789",
            "date": "13-2-2021",
        }
        self.customer = Customer(**self.data)

    def test_create_customer(self):
        self.assertEqual(self.customer.id, "123")
        self.assertEqual(self.customer.name, "Test Customer")
        self.assertEqual(self.customer.address, "Cairo")
        self.assertEqual(self.customer.phone, "0123456789")
        self.assertEqual(self.customer.date, "13-2-2021")

    def test_customer_to_json(self):
        expected = {
            "id": "123",
            "name": "Test Customer",
            "address": "Cairo",
            "phone": "0123456789",
        }
        result = self.customer.to_json()
        self.assertDictEqual(result, expected)
