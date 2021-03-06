"""
A class that take xml page and find property of customer and vehicles
"""
from typing import Dict, List
from bs4 import BeautifulSoup


class ParsedItem:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'xml')

    def find_customer_data(self) -> Dict:
        """
        extract customer data from xml
        :return: return customer data as dictionary
        """
        date = self.soup.find('Date').text
        customer_id = self.soup.find('Customer').attrs['id']
        name = self.soup.find('Name').text
        address = self.soup.find('Address').text
        phone = self.soup.find('Phone').text
        return {
            "_id": customer_id,
            "name": name,
            "address": address,
            "phone": phone,
            "date": date
        }

    def find_vehicles_data(self) -> List:
        """
        extract Vehicle data from xml
        :return: List of vehicle of customer
        """
        vehicles = []
        for match in self.soup.find_all('Vehicle'):
            vehicle_object = {
                "_id": match.get('id'),
                "make": match.find('Make').text,
                "vin_number": match.find('VinNumber').text
            }
            vehicles.append(vehicle_object)
        return vehicles
