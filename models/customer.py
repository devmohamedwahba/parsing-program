class Customer:
    def __init__(self, _id, name, address, phone, date, vehicles=None):
        self.id = _id
        self.name = name
        self.address = address
        self.phone = phone
        self.date = date
        self.vehicles = vehicles

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
        }

    def add_vehicles(self, vehicles):
        self.vehicles = vehicles
