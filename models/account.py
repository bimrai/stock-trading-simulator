from models.transaction import Transaction_History

# account class
class Account:
    def __init__(self, user, balance, stocks, total_invested, transaction_log):
        self.user = user
        self.balance = balance
        self.stocks = stocks
        self.total_invested = total_invested
        self.transaction_log = transaction_log
    
    def deposit(self): 
        amount = int(input("Deposit \n Enter Deposit Amount: £"))
        self.balance += amount
        # self.transaction_log = amount - want to add deposits and withdrawals to the transaction feature to reflect true/all activity
        
        new_transaction = Transaction_History("DEPOSIT", amount, "+")
        self.transaction_log.append(new_transaction)
        
        print("____________________________________________")
        print(f"You have successfully deposited £{amount:,.2f} \nUpdated Balance: £{self.balance:,.2f}")
    
    def check_balance(self):
        print("____________________________________________")
        print(f"Balance \n Current Balance: £{self.balance:,.2f}")
        
    def withdraw(self):
        while True:
            print("____________________________________________")
            withdraw = int(input("Withdraw \n Enter Withdrawal Amount: £"))
            
            if withdraw <= self.balance:
                self.balance = self.balance - withdraw
                print(f"You have successfully withdrawn £{withdraw:,.2f} \n Updated Balance: £{self.balance:,.2f}")

                new_transaction = Transaction_History("WITHDRAW", withdraw, "-")
                self.transaction_log.append(new_transaction)

                break
            elif withdraw > self.balance:
                print("Insufficent Funds")
                continue
                
    def portfolio(self): 
            print("____________________________________________")
            print("Portfolio")
            print(f"Balance: £{self.balance:,.2f}")
            print(f"Total Invested: £{self.total_invested:,.2f}")
            for stock in self.stocks:
                stock.show_stock()
                
    def transactions(self):
        print("____________________________________________")
        print("Transaction History")
        print(f"Balance: £{self.balance:,.2f}")
        print(f"Total Invested: £{self.total_invested:,.2f}")
        
        for log in self.transaction_log:
            log.show_transaction()