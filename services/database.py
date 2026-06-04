import sqlite3
from models.account import Account
from models.stock import Stock
from models.transaction import Transaction_History

# connection and cursor 

def create_table():
    
    #connect to database
    connection = sqlite3.connect('portfolio.db')

    # cursor allows us to interact with the db through sql commands
    # allowing us to create/modify tables within db

    # my account table 
    cursor = connection.cursor()

    command1 = """CREATE TABLE IF NOT EXISTS account(
        user TEXT,
        balance REAL,
        total_investment REAL 
        )"""
        
    cursor.execute(command1)

    # next is my stocks table
    command2 = """CREATE TABLE IF NOT EXISTS stocks(
        stock_name TEXT,
        ticker TEXT,
        shares REAL,
        avg_price REAL,
        stock_total REAL
        )"""
        
    cursor.execute(command2)

    # finally the transaction table

    command3 = """CREATE TABLE IF NOT EXISTS transactions(
        transaction_name TEXT,
        transaction_amount REAL,
        transaction_type TEXT
        )"""

    cursor.execute(command3)
    
    connection.commit()
    connection.close()
    

# this function saves the data from the program
def save_account(account):
    
    connection = sqlite3.connect('portfolio.db')
    cursor = connection.cursor()
    
    insert_account = """INSERT INTO account (user, balance, total_invested) VALUES (?, ?, ?)"""
    
    cursor.execute(insert_account, (account.user, account.balance, account.total_invested))
    
    insert_stock = """INSERT INTO stocks (stock_name, ticker, shares, avg_price, stock_total) VALUES (?, ?, ?, ?, ?)"""
    
    for stock in account.stocks:
        cursor.execute(insert_stock, (stock.stock_name, stock.ticker, stock.shares, stock.avg_price, stock.stock_total))
        
    insert_transactions = """INSERT INTO transactions (transaction_name, transaction_amount, transaction_type) VALUES (?, ?, ?)"""
    
    for transaction in account.transaction_log:
        cursor.execute(insert_transactions, (transaction.transaction_name, transaction.transaction_amount, transaction.transaction_type))
    
    connection.commit()
    connection.close()

