import schedule
import time
from datetime import datetime
from data_fetch import fetch_data
from analytics import optimize_portfolio
from data_cleaning import clean_data
from database import get_historical_performance


def job():
    """Fetch new stock data and update SQL database."""
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "TLT", "^GSPC"]
    print(f"[{datetime.now()}] Fetching latest stock data...")
    fetch_data(tickers)
    print(f"[{datetime.now()}] Data updated successfully.")

# Schedule job to run daily at market close (4:30 PM EST)
schedule.every().day.at("16:30").do(job)

if __name__ == "__main__":
    print("Scheduler running...")
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute
