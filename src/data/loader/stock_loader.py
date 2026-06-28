import yfinance as yf
import pandas as pd
from datetime import datetime
import os

DATA_DIR = "data/raw"

def download_stock(symbol="AAPL", start="2020-01-01", end=None):
    """
    Download historical stock data and save as CSV.
    """

    if end is None:
        end = datetime.today().strftime('%Y-%m-%d')

    # Download data
    df = yf.download(symbol, start=start, end=end)

    # Create folder if it doesn't exist
    os.makedirs(DATA_DIR, exist_ok=True)

    # Save file
    file_path = os.path.join(DATA_DIR, f"{symbol}.csv")
    df.to_csv(file_path)

    print(f"Saved {symbol} data to {file_path}")
    return df


if __name__ == "__main__":
    # Test run
    data = download_stock("AAPL")
    print(data.head())