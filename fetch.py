# fetch.py
from yahooquery import Ticker
from datetime import datetime

def get_price(symbol):
    try:
        ticker = Ticker(symbol)
        price = ticker.price['regularMarketPrice']
        return price, datetime.now()
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None, None

def get_fx_to_thb(currency):
    try:
        pair = f"{currency}THB=X"
        ticker = Ticker(pair)
        fx_rate = ticker.price['regularMarketPrice']
        return fx_rate, datetime.now()
    except Exception as e:
        print(f"Error fetching FX data for {currency} to THB: {e}")
        return None, None
