"""
main app concern is to get some functionality to deal with argument
that enter python program
"""
import sys
import logging

logging.basicConfig(
                    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    level=logging.DEBUG,
                    datefmt='%d-%m-%Y %H:%M:%S',
                    filename='logs.txt')

logger = logging.getLogger(__name__)


class Arguments:
    @classmethod
    def get_format_of_file(cls):
        """
           helper function that return format of file
           :return: format of file
           """
        try:
            file_format = sys.argv[1]
        except Exception as e:
            logger.info(f'{e}')
        else:
            return file_format

    @classmethod
    def get_first_file_name(cls):
        """
           helper function that return name of customer file
           :return: name of customer file
           """
        try:
            first_arg = sys.argv[2]
        except Exception as e:
            logger.info(f'{e}')
        else:
            return first_arg

    @classmethod
    def get_second_file_name(cls):
        """
           helper function that return name of vehicle file
           :return: name of vehicle file
           """
        try:
            second_arg = sys.argv[3]
        except Exception as e:
            logger.info(f'{e}')
        else:
            return second_arg
