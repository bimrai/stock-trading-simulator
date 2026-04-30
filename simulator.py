from models.account import Account
from models.stock import Stock
from models.transaction import Transaction_History
from data.stocks import stock_list

def investment_simulator():
    
    # class object created           
    account = Account("BIM117", 0, [], 0, [])
    
    while True:
        # menu
        print("____________________________________________")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Stock Market")
        print("5. Portfolio")
        print("6. Transaction History")
        print("0. Logout")
        print("____________________________________________")
        # user option input for menu 
        menu_option = int(input("Please Choose An Option: "))
        
        # handle non accepted inputs
        while menu_option not in range(0, 7):
            menu_option = int(input("Invalid! Please Choose An Option: "))
        
        # deposit
        if menu_option == 1:
            account.deposit()
           
        #withdrawal 
        if menu_option == 2:
            account.withdraw()
          
        # check current balance  
        if menu_option == 3:
            account.check_balance()
            

        # implement API to reduce repeated logic for remaining stocks
        # stock market   
        if menu_option == 4:
            
            print("Stock Market:")
            
            for i, company in enumerate(stock_list.keys(), start = 1):
                print(f"{i}. {company}")
            
            print("0. Back")
            
            print("____________________________________________")
            stock_choice = int(input("Please Select An Option: "))
            
            # apple stock purchase
            if stock_choice == 1:
                apple_stock = 189.83
                print("____________________________________________")
                print(f"Selected Apple Stock: \n Apple Stock Current Price: £{apple_stock:,.2f} | Current Balance: £{account.balance:,.2f}")
                
                print("Please choose: \n 1. Buy \n 2. Sell \n 0. Back")
                stock_trade = int(input("Please Select An Option: "))
                
                while stock_trade == 1:
                    amount = int(input("Apple Stock - Enter Purchase Amount: £"))
                    
                    apple_shares = amount / apple_stock
                    
                    # buying power check + confirm purchase
                    if account.balance >= amount and account.balance > apple_stock:
                        print(f"Please confirm your purchase:")
                        print(f"Apple Stock Purchase: £{amount:,.2f}, Shares: {apple_shares:,.4f} \n 1. Confirm \n 0. Cancel")
                        confirm = int(input("Please Select An Option: "))
                        
                        # purchase overview
                        if confirm == 1:
                            print(f"Transaction Complete! \n You have SUCCESSFULLY PURCHASED {apple_shares:,.4f} Shares of Apple Stock worth about £{amount:,.2f}.")
                            account.balance -= amount
                            account.total_invested += amount
                            # account.stock_invested
                            
                            # check if stock already exists or needs to be created
                            found = False
                            
                            for stock in account.stocks:
                                if stock.stock_name == "Apple":
                                    stock.shares += apple_shares
                                    stock.stock_total += amount
                                    found = True
                                    break
                                
                            if not found:
                                new_stock = Stock("Apple", apple_shares, apple_stock, amount)
                                account.stocks.append(new_stock)
                            
                            new_transaction = Transaction_History("APPLE", amount, "PURCHASE")
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
                    amount = int(input("Apple Stock - Enter Sell Amount: £"))
                    
                    apple_shares = amount / apple_stock

                    if account.total_invested > amount:
                        print("Please confirm your sell:")
                        print(f"Apple Stock Sell: £{amount:,.2f}, Shares: {apple_shares:,.4f} \n 1. Confirm \n 0. Cancel")
                        
                        confirm = int(input("Please Select An Option: "))
                        
                        # seeing if while implementation will solve edge cases
                        # while confirm:
                        #     # money logic
                        #     account.total_invested -= amount
                        #     account.balance += amount

                        #     #transaction logic
                        #     new_transaction = Transaction_History("APPLE", amount, "SOLD")
                        #     account.transaction_log.append(new_transaction)

                        #     print(f"Transaction Complete! \n You have SUCCESSFULLY SOLD {apple_shares:,.4f} Shares of Apple Stock worth about £{amount:,.2f}.")
                            
                        #     break

                        # throws an error for Stock where stock_total not attribute in Stock. Fix it!!

                        if confirm == 1:
                            # money logic
                            account.total_invested -= amount
                            account.balance += amount

                            #transaction logic
                            new_transaction = Transaction_History("APPLE", amount, "SOLD")
                            account.transaction_log.append(new_transaction)

                            # trying to solve the problem where portfolio should update new price/shares after selling
                            # account.stock_total -= amount
                            # account.shares -= apple_shares

                            print(f"Transaction Complete! \n You have SUCCESSFULLY SOLD {apple_shares:,.4f} Shares of Apple Stock worth about £{amount:,.2f}.")
                            
                            break
                        elif confirm == 0:
                            break


            # stocks
            if stock_choice == 2:
                print("will add later")
            if stock_choice == 2:
                print("will add later")
            if stock_choice == 2:
                print("will add later")
            if stock_choice == 0:
                continue
        
        if menu_option == 5:
            account.portfolio()
            
        if menu_option == 6:
            account.transactions()
        
        # exit 
        if menu_option == 0:
            print("You have successfully logged out! Have a nice day!")
            break