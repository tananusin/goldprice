# fetch.py
import yfinance as yf
from datetime import datetime
from zoneinfo import ZoneInfo  # Available in Python 3.9+

THAILAND_TZ = ZoneInfo("Asia/Bangkok")

def get_price(symbol):
    symbol_clean = str(symbol).strip().upper()
    if symbol_clean.startswith(("CASH", "BOND")):
        return 1.0, datetime.now(THAILAND_TZ)
    try:
        ticker = yf.Ticker(symbol_clean)
        data = ticker.history(period="1d")
        if data.empty:
            return None, None
        price = data["Close"].iloc[-1]
        timestamp = data.index[-1].astimezone(THAILAND_TZ)
        return price, timestamp
    except Exception as e:
        print(f"Error fetching {symbol}: {e}")
        return None, None

def get_fx_to_thb(currency):
    if currency == "THB":
        return 1.0, datetime.now(THAILAND_TZ)
    try:
        pair = f"{currency}THB=X"
        ticker = yf.Ticker(pair)
        data = ticker.history(period="1d")
        if data.empty:
            return None, None
        fx_rate = round(data["Close"].iloc[-1], 2)
        timestamp = data.index[-1].astimezone(THAILAND_TZ)
        return fx_rate, timestamp
    except Exception as e:
        print(f"Error fetching FX {currency}THB: {e}")
        return None, None
