from models.api import get_stock_data

def market():
    stock_list = []
    
    for ticker in ["AAPL", "NVDA", "TSLA", "META", "AMZN"]:
        data = get_stock_data(ticker)
        stock_list.append(data)
        
    return stock_list