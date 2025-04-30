# fetch.py
import requests
from datetime import datetime

try:
    # Attempt to access the API key from Streamlit secrets
    FMP_API_KEY = st.secrets["api_keys"]["fmp_api_key"]
    st.write("API Key loaded successfully!")
except KeyError as e:
    st.write(f"Error: Key not found: {e}")

def get_gold_price():
    url = f"https://financialmodelingprep.com/api/v3/quote/XAUUSD?apikey={FMP_API_KEY}"
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

def get_usd_to_thb():
    url = f"https://financialmodelingprep.com/api/v3/fx/USDTHB?apikey={FMP_API_KEY}"
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

