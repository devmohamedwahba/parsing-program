"""
main app concern with run main core functionality of app
"""
from utils.arguments import Arguments
from models.customer import Customer
from models.vehicle import Vehicle
from models.transactin import Transaction
from models.transaction_export import TransactionExport
from utils.helper import save_data_to_json_file
from datetime import datetime
from resource.csv_parser import CsvParser
from resource.xml_parser import XmlParser

FIRST_ARGUMENT = Arguments.get_first_file_name()
SECOND_ARGUMENT = Arguments.get_second_file_name()


def main():
    file_format = Arguments.get_format_of_file()
    if file_format == 'csv':
        csv_parser = CsvParser(FIRST_ARGUMENT, SECOND_ARGUMENT)
        customer_data = csv_parser.extract_customer_data()
        vehicle_data = csv_parser.extract_vehicle_data()
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

            result = csv_parser.generate_json_file_structure(customer)

            csv_parser.save_data_as_json(result)

    if file_format == 'xml':
        xml_parser = XmlParser(FIRST_ARGUMENT)
        customer_data = xml_parser.extract_customer_data()
        vehicle_data = xml_parser.extract_vehicle_data()

        current_customer = Customer(**customer_data)
        all_vehicles = [Vehicle(**vehicle) for vehicle in vehicle_data]
        current_customer.add_vehicles(all_vehicles)

        result = xml_parser.generate_json_file_structure(current_customer)
        xml_parser.save_data_as_json(result)


if __name__ == '__main__':
    main()
