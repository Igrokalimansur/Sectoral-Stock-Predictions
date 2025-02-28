import pandas as pd
import requests
import json
import time

# Read tickers from the CSV (assumes header "Ticker")
tickers_df = pd.read_csv('sp500_tickers.csv')
tickers_list = tickers_df['Ticker'].tolist()

api_key = 'WGV2WV2QE4UT4DS0'
function = 'EARNINGS'  # Change to 'BALANCE_SHEET' or 'CASH_FLOW' as needed
all_data = []

for idx, ticker in enumerate(tickers_list, start=1):
    print(f"Processing {idx}/{len(tickers_list)}: {ticker}")
    url = f'https://www.alphavantage.co/query?function={function}&symbol={ticker}&apikey={api_key}'
    try:
        response = requests.get(url)
        data = response.json()
        if 'quarterlyEarnings' in data:
            df_ticker = pd.json_normalize(data['quarterlyEarnings'])
            df_ticker['Ticker'] = ticker
            all_data.append(df_ticker)
        else:
            print(f"No quarterlyEarnings data for {ticker}.")
    except Exception as e:
        print(f"Error processing {ticker}: {e}")
    #time.sleep(0.81)  # Adjust delay if necessary

if all_data:
    final_df = pd.concat(all_data, ignore_index=True)
    final_df.to_csv('sp500_earnings.csv', index=False)
    print("CSV file 'sp500_earnings.csv' created and saved.")
else:
    print("No data was collected.")