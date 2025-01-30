import yfinance as yf
import pandas as pd
from database import save_to_database

def fetch_data(tickers, start_date="2018-01-01", end_date=None):
    """Fetch stock data and store in SQLite."""
    
    # Fetch data
    data = yf.download(tickers, start=start_date, end=end_date)

    # Print column structure for debugging
    print(f"📊 Available Columns: {data.columns}")

    # Extract 'Close' prices from MultiIndex columns
    if "Close" in data.columns.get_level_values(0):
        data = data["Close"]
    else:
        raise ValueError("XXXX Error: 'Close' price data not found.")

    if data.empty:
        print("XXXX Error: No data fetched from Yahoo Finance. Check ticker symbols.")
        return

    # Store data in SQL
    for ticker in tickers:
        if ticker in data.columns:
            df = data[[ticker]].dropna().reset_index()
            df.columns = ["date", "adjusted_close"]  # Renaming for consistency
            save_to_database(df, ticker)
        else:
            print(f"⚠️ Warning: No data found for {ticker}, skipping.")

    print("✅ Data fetched and stored successfully!")

if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "GOOGL", "TSLA", "AMZN", "TLT", "^GSPC"]
    fetch_data(tickers)