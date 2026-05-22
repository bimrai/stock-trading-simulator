from models.account import Account
from models.stock import Stock
from models.transaction import Transaction_History
from data.stocks import market


def trade_stock(account, stock_name, stock_price, ticker):

    print("____________________________________________")
    print(f"Selected {stock_name} Stock: \n {stock_name} Current Price: £{stock_price:,.2f} | Current Balance: £{account.balance:,.2f}")

    print("Please choose: \n 1. Buy \n 2. Sell \n 0. Back")
    stock_trade = int(input("Please Select An Option: "))

    while stock_trade == 1:
        amount = int(input(f"{stock_name} - Enter Purchase Amount: £"))
        
        stock_shares = amount / stock_price
        
        # buying power check + confirm purchase
        if account.balance >= amount and account.balance > stock_price:
            print(f"Please confirm your purchase:")
            print(f"{stock_name} Purchase: £{amount:,.2f}, Shares: {stock_shares:,.4f} \n 1. Confirm \n 0. Cancel")
            confirm = int(input("Please Select An Option: "))
            
            # purchase overview
            if confirm == 1:
                print(f"Transaction Complete! \n You have SUCCESSFULLY PURCHASED {stock_shares:,.4f} Shares of {stock_name} worth about £{amount:,.2f}.")
                account.balance -= amount
                account.total_invested += amount
                
                
                # check if stock already exists or needs to be created
                found = False
                
                for stock in account.stocks:
                    if stock.stock_name == stock_name:
                        old_shares = stock.shares
                        stock.shares += stock_shares
                        stock.avg_price = (old_shares * stock.avg_price + stock_shares * stock_price) / stock.shares
                        stock.stock_total += amount
                        found = True
                        break
                    
                if not found:
                    new_stock = Stock(stock_name, stock_shares, stock_price, amount)
                    account.stocks.append(new_stock)
                
                new_transaction = Transaction_History(stock_name, amount, "PURCHASE")
                account.transaction_log.append(new_transaction)
                
                print(f"Updated Balance: £{account.balance:,.2f}")
                break
            else:
                break
            
        # option to add more balance or return to main menu if not
        elif account.balance < amount:
            print(f"Insufficient Funds: £{account.balance:,.2f}.")
            print("Would you like to add funds?")
            print("1. Yes")
            print("0. No")
            pick = int(input("Enter 1 or 0: "))
            
            if pick == 1:
                account.deposit()
                print("____________________________________________")
            else:
                continue

    while stock_trade == 2:
        amount = int(input(f"{stock_name} - Enter Sell Amount: £"))
        
        stock_shares = amount / stock_price

        if account.total_invested > amount:
            print("Please confirm your sell:")
            print(f"{stock_name} Sell: £{amount:,.2f}, Shares: {stock_shares:,.4f} \n 1. Confirm \n 0. Cancel")
            
            confirm = int(input("Please Select An Option: "))

            if confirm == 1:
                # money logic
                account.total_invested -= amount
                account.balance += amount
                
                for stock in account.stocks:
                    if stock.stock_name == stock_name:
                        stock.shares -= stock_shares
                        stock.stock_total -= amount
                        found = True
                        break
                
                

                #transaction logic
                new_transaction = Transaction_History(stock_name, amount, "SOLD")
                account.transaction_log.append(new_transaction)
                
                print(f"Transaction Complete! \n You have SUCCESSFULLY SOLD {stock_shares:,.4f} Shares of {stock_name} worth about £{amount:,.2f}.")
                
                break
            elif confirm == 0:
                break
    
    
    