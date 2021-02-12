"""
main app concern with run main core functionality of app
"""
from utils.arguments import Arguments
from models.customer import Customer
from models.vehicle import Vehicle
from resource.csv_parser import CsvParser
from resource.xml_parser import XmlParser


def main():
    file_format = Arguments.get_format_of_file()

    if file_format == 'csv':
        first_argument = Arguments.get_first_file_name()
        second_argument = Arguments.get_second_file_name()

        csv_parser = CsvParser(first_argument, second_argument)

        customer_data = csv_parser.extract_customer_data()
        vehicle_data = csv_parser.extract_vehicle_data()

        customers = [Customer(**customer) for customer in customer_data]
        for customer in customers:
            vehicles = [Vehicle(**vehicle) for vehicle in vehicle_data if customer.id == vehicle.get('owner_id')]
            customer.add_vehicles(vehicles)

            result = csv_parser.generate_json_file_structure(customer)
            csv_parser.save_data_as_json(result)

    if file_format == 'xml':
        first_argument = Arguments.get_first_file_name()

        xml_parser = XmlParser(first_argument)

        customer_data = xml_parser.extract_customer_data()
        vehicle_data = xml_parser.extract_vehicle_data()

        current_customer = Customer(**customer_data)
        all_vehicles = [Vehicle(**vehicle) for vehicle in vehicle_data]
        current_customer.add_vehicles(all_vehicles)

        result = xml_parser.generate_json_file_structure(current_customer)
        xml_parser.save_data_as_json(result)


if __name__ == '__main__':
    main()
