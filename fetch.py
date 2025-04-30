# fetch.py
import requests
from datetime import datetime

def get_gold_price(api_key):
    url = f"https://financialmodelingprep.com/api/v3/quote/XAUUSD?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                return float(data[0].get("price", 0)), datetime.now()
        except Exception as e:
            print(f"Error fetching data for gold: {e}")
            return None, None
    return None, None

def get_usd_to_thb(api_key):
    url = f"https://financialmodelingprep.com/api/v3/fx/USDTHB?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                return float(data[0].get("bid", 0)), datetime.now()
            elif isinstance(data, dict):
                return float(data.get("bid", 0)), datetime.now()
        except Exception as e:
            print(f"Error fetching FX data for USD to THB: {e}")
            return None, None
    return None, None

