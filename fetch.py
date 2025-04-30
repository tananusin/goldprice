# fetch.py
import yfinance as yf
from datetime import datetime

def get_price(symbol):
    """Fetch price data using YFinance"""
    symbol_clean = str(symbol).strip().upper()
    try:
        ticker = yf.Ticker(symbol_clean)
        price = ticker.info['regularMarketPrice']  # YFinance uses this structure
        return price, datetime.now()
    except Exception as e:
        print(f"Error fetching data for {symbol} from YFinance: {e}")
        return None, None

def get_fx_to_thb(currency):
    """Fetch FX rate data using YFinance"""
    try:
        pair = f"{currency}THB=X"
        ticker = yf.Ticker(pair)
        fx_rate = ticker.history(period="1d")["Close"].iloc[-1]  # YFinance requires historical data
        return fx_rate, datetime.now()
    except Exception as e:
        print(f"Error fetching FX data for {currency} to THB from YFinance: {e}")
        return None, None
