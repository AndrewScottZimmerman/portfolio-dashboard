import sqlite3
import pandas as pd

conn = sqlite3.connect("database/portfolio.db")  # Ensure correct path
df = pd.read_sql("SELECT * FROM stock_prices LIMIT 5;", conn)
conn.close()

print(df)