# fetch.py
import yfinance as yf
from datetime import datetime

def get_price(symbol):
    symbol_clean = str(symbol).strip().upper()
    if symbol_clean.startswith(("CASH", "BOND")):
        return 1.0, datetime.now()
    try:
        ticker = yf.Ticker(symbol_clean)
        price = ticker.info["regularMarketPrice"]        
        return price, datetime.now()
    except:
        return None, None

def get_fx_to_thb(currency):
    if currency == "THB":
        return 1.0
    try:
        pair = f"{currency}THB=X"
        fx = yf.Ticker(pair).history(period="1d")
        fx_rate = round(fx["Close"].iloc[-1], 2)
        return fx_rate, datetime.now()
    except:
        return None, None
