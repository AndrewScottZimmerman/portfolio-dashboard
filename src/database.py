import sqlite3
import pandas as pd
import os

# Ensure the database directory exists
DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../database/portfolio.db"))
DB_DIR = os.path.dirname(DB_PATH)
if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)

def create_database():
    """Create SQLite database and tables."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS stock_prices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        symbol TEXT,
        date TEXT,
        adjusted_close REAL
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS portfolio_performance (
        date TEXT,
        strategy TEXT,
        cumulative_return REAL
    )''')

    conn.commit()
    conn.close()

def save_to_database(df, symbol):
    """Save stock data to SQLite."""
    conn = sqlite3.connect(DB_PATH)
    df["symbol"] = symbol
    df.to_sql("stock_prices", conn, if_exists="append", index=False)
    conn.close()

def query_stock_data(symbol):
    """Query stock data from database."""
    conn = sqlite3.connect(DB_PATH)
    query = f"SELECT date, adjusted_close FROM stock_prices WHERE symbol = '{symbol}'"
    df = pd.read_sql(query, conn, parse_dates=["date"])
    conn.close()
    return df

def get_historical_performance():
    """Retrieve past portfolio performance from SQL."""
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM portfolio_performance", conn, parse_dates=["date"])
    conn.close()
    return df

if __name__ == "__main__":
    create_database()
    print(f"Database created at: {DB_PATH}")