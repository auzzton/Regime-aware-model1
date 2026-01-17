
import yfinance as yf
import pandas as pd

TICKERS = ["GS", "NVDA", "BRK-B", "C", "JPM", "^VIX"]
START_DATE = "2010-01-01"
END_DATE = "2024-12-15"

print("Downloading data...")
# Replicate the exact call from main.py
data = yf.download(TICKERS, start=START_DATE, end=END_DATE, auto_adjust=True)["Close"].dropna(how='all')

print(f"Data shape: {data.shape}")
print(data.head())
print(data.tail())

print("\nCalculating returns...")
returns = data.pct_change()
print("Returns head (before dropna):")
print(returns.head())

returns = returns.dropna()
print(f"Returns shape (after dropna): {returns.shape}")
