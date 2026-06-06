# Stock Trading Simulator

A Python CLI application that simulates stock trading with live market prices, portfolio tracking, and persistent data storage.

## Features

- **Live Stock Prices** - real-time data via Yahoo Finance API
- **Buy & Sell Stocks** - trade from a selection of 5 major stocks (with ease of adding more) 
- **Portfolio Tracking** - view holdings, average price, and unrealised P&L
- **Realised P&L** - profit/loss calculated on every sell
- **Transaction History** - full log of all buys, sells, deposits and withdrawals
- **Data Persistence** - portfolio and account data saved between sessions via SQLite

## Stocks Available (Can add more if needed)

| Ticker | Company |
|--------|---------|
| AAPL | Apple Inc. |
| NVDA | NVIDIA Corporation |
| TSLA | Tesla, Inc. |
| META | Meta Platforms, Inc. |
| AMZN | Amazon.com, Inc. |

## Project Structure

```
stock-trading-simulator/
├── data/
│   └── stocks.py           # Market data fetching
├── models/
│   ├── account.py          # Account class
│   ├── api.py              # Yahoo Finance API wrapper
│   ├── stock.py            # Stock class
│   └── transaction.py      # Transaction history class
├── services/
│   ├── database.py         # SQLite persistence layer
│   └── trade_stock.py      # Core trading logic
├── main.py
└── simulator.py            # Main application loop
```

## Setup & Installation

**Requirements:**
- Python 3
- yfinance

**Install dependencies:**
```bash
pip install yfinance
```

**Run the application:**
```bash
python main.py
```

## Usage

On launch you'll be presented with a menu:

```
1. Deposit
2. Withdraw
3. Check Balance
4. Stock Market
5. Portfolio
6. Transaction History
0. Logout
```

Navigate to Stock Market to browse live prices and trade. Your portfolio and balance are automatically saved when you log out.

## Technical Highlights

- Object-oriented design with separate model classes for Account, Stock, and Transaction
- Weighted average cost basis calculation on each buy
- Scalable trade logic - adding new stocks requires no changes to core flow
- SQLite database for persistent storage across sessions
- Live price data fetched via `yfinance` at runtime

## Built With

- Python 3
- SQLite3 (built-in)
- yfinance
