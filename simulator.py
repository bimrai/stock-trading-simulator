from models.account import Account
from models.stock import Stock
from models.transaction import Transaction_History
from data.stocks import market
from services.trade_stock import trade_stock

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
        
        # handle non accepted inputs        
        while True:
            try:
                menu_option = int(input("Please Choose An Option: ")) # user option input for menu 
                
                # validates input and catches errors without crashing program
                if menu_option in range(0, 7):
                    break
                else:
                    print("Invalid! Please Choose An Option.")
            except:
                print("Invalid! Please Choose An Option.")
        
        # deposit
        if menu_option == 1:
            account.deposit()
           
        #withdrawal 
        if menu_option == 2:
            account.withdraw()
          
        # check current balance  
        if menu_option == 3:
            account.check_balance()
            
        # stock market   
        if menu_option == 4:
            print("Stock Market:")
            
            stocks = market()
            
            for i, stock in enumerate(stocks, start=1):
                print(f'{i}. ({stock["ticker"]}), {stock["name"]}: £{stock["price"]:,.2f}')
            
            print("0. Back")
            print("____________________________________________")
            stock_choice = int(input("Please Select An Option: "))

            if 1 <= stock_choice <= len(stocks):
                chosen = stocks[stock_choice - 1]
                trade_stock(account, chosen["name"], chosen["price"], chosen["ticker"])
        
        if menu_option == 5:
            account.portfolio()
            
        if menu_option == 6:
            account.transactions()
        
        # exit 
        if menu_option == 0:
            print("You have successfully logged out! Have a nice day!")
            break