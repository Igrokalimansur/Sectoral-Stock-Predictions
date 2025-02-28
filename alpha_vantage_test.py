import requests
import pandas as pd
import json

symbol = 'TDG'
api = 'WGV2WV2QE4UT4DS0'
type = 'EARNINGS'
url = f'https://www.alphavantage.co/query?function={type}&symbol={symbol}&apikey={api}'

response = requests.get(url)
data = response.json()

print(data)

# with open('tdg_earnings.json', 'w') as json_file:
#     json.dump(data, json_file)
#
# print("tdg quarterly JSON file created and saved.")
#
# with open('tdg_earnings.json', 'r') as f:
#     data = json.load(f)
#
# df = pd.json_normalize(data['quarterlyReports'])
# df['Ticker'] = 'TDG'
#
# df.to_csv('tdg_quarterly.csv', index=False)
# print("TDG quarterly CSV file created and saved.")
#
