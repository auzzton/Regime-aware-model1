
import yfinance as yf
import pandas as pd

TICKERS = ["GS", "NVDA", "BRK-B", "C", "JPM", "^VIX"]
START_DATE = "2010-01-01"
END_DATE = "2024-12-15"

print("Downloading data...")
# Disable progress to keep output clean
data = yf.download(TICKERS, start=START_DATE, end=END_DATE, progress=False)

print("\n--- DATA INFO ---")
print("Columns:", data.columns)
if isinstance(data.columns, pd.MultiIndex):
    print("Columns Levels:", data.columns.levels)

print("\n--- ATTEMPTING ACCESS ---")
try:
    adj_close = data["Adj Close"]
    print("Accessed 'Adj Close' successfully.")
    print(adj_close.head())
except KeyError as e:
    print(f"Failed to access 'Adj Close': {e}")
    # Try one level up or see what's available
    print("Available top-level keys:", data.columns.get_level_values(0).unique())
