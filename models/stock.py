# stock class
class Stock:
    def __init__(self, stock_name, ticker, shares, avg_price, stock_total):
        self.stock_name = stock_name
        self.ticker = ticker
        self.shares = shares
        self.avg_price = avg_price
        self.stock_total = stock_total
        
    def show_stock(self):
        print(f"• {self.stock_name} \n Shares: {self.shares:.4f} Total Invested: £{self.stock_total:,.2f} \n Average Price: £{self.avg_price:,.2f}")