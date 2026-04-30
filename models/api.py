import yfinance as yf

def get_stock_data(symbol):
    
    stock = yf.Ticker(symbol)

    info = stock.info
    price = stock.fast_info.get("lastPrice")

    name = info.get("longName") or info.get("shortName") or symbol

    return {
        "ticker": symbol.upper(),
        "name": name,
        "price": price
    }