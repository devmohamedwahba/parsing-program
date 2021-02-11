from utils.arguments import Arguments

file_format = Arguments.get_format_of_file()
customer_file_name = Arguments.get_first_file_name()


class TransactionExport:
    def __init__(self, transaction):
        self.transaction = transaction

    def to_export(self):
        return {
            "file_name": f'{file_format}/{customer_file_name}',
            "transaction": self.transaction.to_json()
        }
