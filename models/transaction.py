class Transaction_History:
        def __init__(self, transaction_name, transaction_amount, transaction_type):
            self.transaction_name = transaction_name
            self.transaction_amount = transaction_amount
            self.transaction_type = transaction_type

        def show_transaction(self):
            print(f"{self.transaction_name}: £{self.transaction_amount:,.2f} {self.transaction_type}")