import os
import unittest
from utils.helper import get_data_from_csv_file, save_data_to_json_file, read_xml_file


class TestHelper(unittest.TestCase):
    def test_get_data_from_csv_file(self):
        csv_path = 'task/input_data/csv/customers.csv'
        expected = [['ID5410', 'Melissa T Miller', '2837  Fidler Drive', '210-624-7306', '31/01/2020'],
                    ['ID9857', 'Daniel I Walker', '3853  Hilltop Street', '413-655-7397', '25/04/2020'],
                    ['ID6651', 'Pauline J Buxton', '1927  Pinnickinick Street', '360-727-9275', '16/03/2020']]

        result = get_data_from_csv_file(csv_path)
        self.assertEqual(result, expected)

    def test_save_data_to_json_file(self):
        data = {'file_name': 'xml/task/input_data/xml/customer1.xml',
                'transaction':
                    {'date': '2021-12-07',
                     'customer': {'id': 'ID1011200',
                                  'name': 'Shirish Suchak',
                                  'address': '1429  Joyce Street',
                                  'phone': '252-414-7396'}}}

        save_data_to_json_file(data=data, file_name=f'output/test.json')
        self.assertTrue(os.path.exists('output/test.json'))

    def test_read_xml_file(self):
        xml_path = 'task/input_data/xml/customer1.xml'
        result = read_xml_file(xml_path)
        self.assertTrue("<Name>Shirish Suchak</Name>" in result)