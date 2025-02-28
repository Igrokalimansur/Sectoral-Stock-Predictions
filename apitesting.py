import pandas as pd
import requests
import json
import time

# Read tickers from the CSV (assumes header "Ticker")
tickers_df = pd.read_csv('sp500_tickers.csv')
tickers_list = tickers_df['Ticker'].tolist()

api_key = 'WGV2WV2QE4UT4DS0'
function = 'INTRADAY'
all_data = []

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=1min&apikey=WGV2WV2QE4UT4DS0'

response = requests.get(url)
data = response.json()

print(data)

