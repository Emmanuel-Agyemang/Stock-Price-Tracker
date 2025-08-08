# stock_price_tracker_live_input.py

import yfinance as yf
import matplotlib.pyplot as plt

def fetch_and_plot_stock(ticker, period='1mo', interval='1d'):
    """
    Fetches stock data for a given ticker and plots the closing price along with
    20-day and 50-day moving averages.
    """
    data = yf.download(ticker, period=period, interval=interval)
    
    if data.empty:
        print(f"No data found for {ticker} with period={period} and interval={interval}.")
        return
    
    data['MA20'] = data['Close'].rolling(window=20).mean()
    data['MA50'] = data['Close'].rolling(window=50).mean()
    
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label='Close Price', color='blue')
    plt.plot(data.index, data['MA20'], label='20-day MA', color='orange')
    plt.plot(data.index, data['MA50'], label='50-day MA', color='green')
    plt.title(f'{ticker} Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.legend()
    plt.grid(True)
    plt.show()
    
def get_live_price(ticker):
    """
    Fetches the most recent market price for the given ticker symbol.
    """
    stock = yf.Ticker(ticker)
    live_price = stock.info.get('regularMarketPrice', None)
    
    if live_price:
        print(f"Current price of {ticker}: ${live_price}")
    else:
        print(f"Live price not available for {ticker}")

def get_user_input():
    """
    Prompt user for ticker, period, and interval with some validation.
    """
    ticker = input("Enter the stock ticker symbol (e.g., AAPL): ").strip().upper()
    
    valid_periods = ['1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max']
    period = input(f"Enter period (default '3mo') options {valid_periods}: ").strip().lower()
    if period == '':
        period = '3mo'
    elif period not in valid_periods:
        print("Invalid period entered. Using default '3mo'.")
        period = '3mo'
        
    valid_intervals = ['1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo']
    interval = input(f"Enter interval (default '1d') options {valid_intervals}: ").strip().lower()
    if interval == '':
        interval = '1d'
    elif interval not in valid_intervals:
        print("Invalid interval entered. Using default '1d'.")
        interval = '1d'
        
    # yfinance only supports certain interval-period combos, no strict check here
    return ticker, period, interval

if __name__ == "__main__":
    ticker, period, interval = get_user_input()
    
    get_live_price(ticker)
    fetch_and_plot_stock(ticker, period=period, interval=interval)
