
import yfinance as yf
import pandas as pd
import sys

# Redirect stdout to a file
with open("c:/Projects/Regimeaware1/lumina/debug_output.txt", "w") as f:
    sys.stdout = f
    
    TICKERS = ["GS", "NVDA", "BRK-B", "C", "JPM", "^VIX"]
    START_DATE = "2010-01-01"
    END_DATE = "2024-12-15"

    print("Downloading data...")
    data = yf.download(TICKERS, start=START_DATE, end=END_DATE, progress=False)

    print("\n--- DATA INFO ---")
    print("Columns:", data.columns)
    if isinstance(data.columns, pd.MultiIndex):
        print("Columns Levels:", data.columns.levels)
        print("First column:", data.columns[0])

    print("\nAvailable Level 0 values:", data.columns.get_level_values(0).unique())
