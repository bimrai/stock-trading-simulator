import yfinance as yf

def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    return stock.fast_info["lastPrice"]

print(f'Apple Stock: ${get_stock_price("AAPL"):.2f}')