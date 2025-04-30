# fetch.py
import requests
from datetime import datetime

FMP_API_KEY = st.secrets["api_keys"]["fmp_api_key"]

def get_gold_price():
    url = f"https://financialmodelingprep.com/api/v3/quote/XAUUSD?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                return float(data[0].get("price", 0)), datetime.now()
        except Exception as e:
            print(f"Error fetching data for {symbol} from YFinance: {e}")
            return None, None
    return 0

def get_usd_to_thb():
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
            print(f"Error fetching FX data for {currency} to THB from YFinance: {e}")
            return None, None
    return 0
