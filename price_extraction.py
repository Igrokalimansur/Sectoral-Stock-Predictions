import requests
import pandas as pd
import time

def getmonthlydata(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    if "Monthly Time Series" not in data:
        print(f"No monthly time series for {symbol}")
        return []

    monthly_series = data["Monthly Time Series"]
    records = []

    for date_str, metrics in monthly_series.items():
        records.append({
            "Ticker": symbol,
            "Date": date_str,
            "Open": metrics["1. open"],
            "High": metrics["2. high"],
            "Low": metrics["3. low"],
            "Close": metrics["4. close"],
            "Volume": metrics["5. volume"]
        })

    return records

def main():
    api_key = "WGV2WV2QE4UT4DS0"  # Replace with your paid Alpha Vantage API key
    input_csv = "sp500_tickers.csv"  # CSV must have a 'Ticker' column
    output_csv = "sp500_monthly_data.csv"

    # Read all tickers from the CSV
    tickers_df = pd.read_csv(input_csv)
    tickers_list = tickers_df["Ticker"].tolist()

    all_rows = []

    for i, symbol in enumerate(tickers_list, start=1):
        print(f"Processing {i}/{len(tickers_list)}: {symbol}")
        try:
            rows = getmonthlydata(symbol, api_key)
            all_rows.extend(rows)
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")

        # Pause between requests to avoid hitting rate limits
        time.sleep(1)

    if all_rows:
        # Convert the collected data into a DataFrame
        df = pd.DataFrame(all_rows)

        # Convert numeric columns to floats, if desired
        # This also helps convert strings like '125.5000' into actual floats
        numeric_cols = ["Open", "High", "Low", "Close", "Volume"]
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        # Sort by Ticker and Date (descending) for convenience
        df.sort_values(by=["Ticker", "Date"], ascending=[True, False], inplace=True)

        # Save the final DataFrame to CSV
        df.to_csv(output_csv, index=False)
        print(f"Monthly price data saved to '{output_csv}'.")
    else:
        print("No data was collected.")


if __name__ == "__main__":
    main()