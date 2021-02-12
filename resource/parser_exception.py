"""
Custom Exception to that raise from parsing file
"""


class ParserException(Exception):
    def __init__(self, message):
        super().__init__(message)
