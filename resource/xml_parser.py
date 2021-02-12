"""
class to parse xml file
"""
from typing import Dict, List
from .parser import Parser
from utils.helper import read_xml_file
from resource.soup import ParsedItem
from resource.parser_exception import ParserException


class XmlParser(Parser):
    def __init__(self, customer_file):
        Parser.__init__(self, customer_file)

    def extract_customer_data(self) -> Dict:
        """
        :return:  Dictionary of customer
        """
        try:
            xml_file_as_string = read_xml_file(self.customer_file)
            soup_item = ParsedItem(xml_file_as_string)
            return soup_item.find_customer_data()
        except Exception as e:
            raise ParserException('error in parse customer from xml')

    def extract_vehicle_data(self) -> List:
        """
        :return: list of Dictionary of vehicle
        """
        try:
            xml_file_as_string = read_xml_file(self.customer_file)
            soup_item = ParsedItem(xml_file_as_string)
            return soup_item.find_vehicles_data()
        except Exception as e:
            raise ParserException('error in parse vehicle from xml')
