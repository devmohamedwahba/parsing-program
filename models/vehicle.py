class Vehicle:
    def __init__(self, _id, make, vin_number, owner_id):
        self.id = _id
        self.make = make
        self.vin_number = vin_number
        self.owner_id = owner_id

    def to_json(self):
        return {
            "id": self.id,
            "make": self.make,
            "vin_number": self.vin_number,
        }
