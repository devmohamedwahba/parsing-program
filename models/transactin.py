class Transaction:
    def __init__(self, customer):
        self.customer = customer

    def to_json(self):
        return {
            "date": self.customer.date,
            "customer": self.customer.to_json(),
            "vehicle": [vehicle.to_json() for vehicle in self.customer.vehicles],
        }
