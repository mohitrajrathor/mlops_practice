# python script that retrive current google stock price from google api display it on terminal

import requests
from bs4 import BeautifulSoup


def fetch_price():
    url = "https://www.google.com/finance/quote/GOOG:NASDAQ"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to retrieve page: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    try:
        # Google's price is usually in a <div> with class "YMlKec fxKbKc"
        price_div = soup.find("div", class_="YMlKec fxKbKc")
        if price_div:
            print(f"Current GOOG Stock Price: {price_div.text}")
        else:
            print("Could not find the price element.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    # fetching price
    fetch_price()


if __name__ == "__main__":
    main()
