import yfinance as yf
import pandas as pd
import os

# 1. Define the ticker (e.g., AAPL from the kickoff doc)
ticker_symbol = "AAPL"
ticker = yf.Ticker(ticker_symbol)

print(f"--- Fetching data for {ticker_symbol} ---")

# 2. Fetch 5 years of historical data
hist_data = ticker.history(period="5y")

# 3. Store the data locally as a CSV
output_file = f"{ticker_symbol}_historical_data.csv"
hist_data.to_csv(output_file)

print(f"\n--- Data Head (First 5 Rows) ---")
print(hist_data.head())

print(f"\n--- Data Info (Preprocessing Check for MF-2) ---")
hist_data.info()

print(f"\n[SUCCESS] Data saved to {os.path.abspath(output_file)}")