import pandas as pd

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# MSCI Classification Sectors

sectors = ["Energy", "Materials", "Industrials", "Consumer Discretionary",
        "Consumer Staples", "Health Care", "Financials", "Information Technology",
        "Communication Services", "Utilities", "Real Estate"
    ]

def download_wikipedia_data():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

    tables = pd.read_html(url)

    df = tables[0]

    df = df[['Symbol', 'GICS Sector']]
    df.columns = ['Ticker', 'Sector']

    return df

def main():
    sp500_df = download_wikipedia_data()

    print(sp500_df.head())

    output_filename = 'sp500_tickers.csv'
    sp500_df.to_csv(output_filename, index=False)
    print(f"\nData successfully saved to '{output_filename}'.")

if __name__ == "__main__":
    main()