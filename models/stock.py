# stock class
class Stock:
    def __init__(self, stock_name, shares, buy_price, stock_total):
        self.stock_name = stock_name
        self.shares = shares
        self.buy_price = buy_price
        self.stock_total = stock_total
    
    def show_stock(self):
        print(f"Stock: {self.stock_name} \n Shares: {self.shares:.4f} Total Invested: £{self.stock_total:,.2f} \n Bought Price: £{self.buy_price:,.2f}")