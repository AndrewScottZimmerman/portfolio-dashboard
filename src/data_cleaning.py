import pandas as pd
from database import query_stock_data

def clean_data(symbols):
    """Retrieve & clean stock data from SQL."""
    dfs = []

    for symbol in symbols:
        df = query_stock_data(symbol)

        if df.empty:
            print(f"!!!! Warning: No data found for {symbol}. Skipping.")
            continue

        df = df.rename(columns={"adjusted_close": symbol})  # Match stored column name
        df.set_index("date", inplace=True)

        # Ensure unique index values
        df = df[~df.index.duplicated(keep='first')]

        # Sort index
        df = df.sort_index()

        dfs.append(df)

    if not dfs:
        raise ValueError("XXXX Error: No valid stock data retrieved. Check database population.")

    # Merge data on date, ensuring indexes align properly
    df = pd.concat(dfs, axis=1, join="inner").sort_index()

    # Calculate daily returns
    returns = df.pct_change().dropna()

    return df, returns