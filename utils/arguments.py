"""
main app concern is to get some functionality to deal with argument that enter python program
"""
import sys


class Arguments:
    @classmethod
    def get_format_of_file(cls):
        """
           helper function that return format of file
           :return: format of file
           """
        return sys.argv[1]

    @classmethod
    def get_customer_file_name(cls):
        """
           helper function that return name of customer file
           :return: name of customer file
           """
        return sys.argv[2]

    @classmethod
    def get_vehicle_file_name(cls):
        """
           helper function that return name of vehicle file
           :return: name of vehicle file
           """
        return sys.argv[3]




    # @classmethod
    # def get_arguments(cls):
    #     """
    #     helper function that get all argument
    #     :return: list of argument
    #     """
    #     return sys.argv
    #
    # @classmethod
    # def get_number_of_arguments(cls):
    #     """
    #     helper function that return count of arguments
    #     :return: number of arguments
    #     """
    #     return len(sys.argv)
