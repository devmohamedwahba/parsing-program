"""
main app concern with run main core functionality of app
"""
from utils.arguments import Arguments
from models.customer import Customer
from models.vehicle import Vehicle
from models.transactin import Transaction
from models.transaction_export import TransactionExport
from utils.helper import get_data_from_csv_file, save_data_to_json_file
from datetime import datetime

CUSTOMER_FILE_NAME = Arguments.get_customer_file_name()
VEHICLE_FILE_NAME = Arguments.get_vehicle_file_name()


def main():
    file_format = Arguments.get_format_of_file()
    if file_format == 'csv':
        customer_data = get_data_from_csv_file(CUSTOMER_FILE_NAME)
        vehicle_data = get_data_from_csv_file(VEHICLE_FILE_NAME)

        customers = [
            Customer(_id=line[0], name=line[1], address=line[2], phone=line[3], date=line[4])
            for line in customer_data
        ]

        for customer in customers:
            vehicles = [
                Vehicle(_id=line[0], make=line[1], vin_number=line[2], owner_id=line[3])
                for line in vehicle_data if customer.id == line[3]
            ]
            customer.add_vehicles(vehicles)
            transaction = Transaction(customer)
            result = TransactionExport(transaction).to_export()
            save_data_to_json_file(result, f'output/{datetime.now()}result.json')


if __name__ == '__main__':
    main()
