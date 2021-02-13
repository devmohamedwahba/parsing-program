import unittest
from models.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.data = {
            "_id": "123",
            "make": "Test Vehicle",
            "vin_number": "5555",
            "owner_id": "0123456789",
        }
        self.vehicle = Vehicle(**self.data)

    def test_create_vehicle(self):
        self.assertEqual(self.vehicle.id, "123")
        self.assertEqual(self.vehicle.make, "Test Vehicle")
        self.assertEqual(self.vehicle.vin_number, "5555")
        self.assertEqual(self.vehicle.owner_id, "0123456789")

    def test_vehicle_to_json(self):
        expected = {
            "id": "123",
            "make": "Test Vehicle",
            "vin_number": "5555",
        }
        result = self.vehicle.to_json()
        self.assertDictEqual(result, expected)
