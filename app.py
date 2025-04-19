#app.py
#Goldbartrading
import streamlit as st
from fmp_api import get_gold_price, get_usd_to_thb

# App title
st.title("💰 Gold Bar Cal.")

# Fetch live data
FMP_API_KEY = st.secrets["api_keys"]["fmp_api_key"]
gold_price_oz_usd = get_gold_price(FMP_API_KEY)
usd_to_thb = get_usd_to_thb(FMP_API_KEY)

# Handle errors (returned as strings)
if isinstance(gold_price_oz_usd, str):
    st.error(gold_price_oz_usd)
    gold_price_oz_usd = 0
if isinstance(usd_to_thb, str):
    st.error(usd_to_thb)
    usd_to_thb = 0

# Show fetched prices
st.subheader("📡 Live Market Data")
st.write(f"Fetched Gold Price (USD/OZ): {gold_price_oz_usd:,.0f}")
st.write(f"Fetched USD to THB Exchange Rate: {usd_to_thb:.2f}")
# gold_price_oz_usd = st.number_input("Gold spot 99.99% 1 troy oz (USD)", value=gold_price_oz_usd, format="%.2f") # optional manual override
# usd_to_thb = st.number_input("USD/THB exchange rate", value=usd_to_thb, format="%.2f") # optional manual override

# Budget
st.subheader("📊 Budget Breakdown")

# User Input: Budget
budget = st.number_input("Enter your budget in THB", value=0, step=1000)

# Conversion constants
grams_per_oz = 31.1035
grams_per_baht = 15.244
purity_965 = 0.965

# Calculations
gold_price_per_oz_thb = gold_price_oz_usd * usd_to_thb
gold_price_per_gram_thb = gold_price_per_oz_thb / grams_per_oz
gold_price_1baht_thb = gold_price_per_gram_thb * grams_per_baht * purity_965

# Budget conversion
budget_per_oz = budget / gold_price_per_oz_thb
budget_per_gram = budget / gold_price_per_gram_thb
budget_per_baht = budget / gold_price_1baht_thb

# Outputs
st.write(f"**99.99% gold:** {budget_per_oz:,.2f} troy oz")
st.write(f"**99.99% gold:** {budget_per_gram:,.2f} grams")
st.write(f"**96.50% gold:** {budget_per_baht:,.2f} บาท")

st.subheader("📈 Reference Prices")
st.write(f"**1 troy oz of 99.99% gold =** {gold_price_per_oz_thb:,.0f} THB")
st.write(f"**1 gram of 99.99% gold =** {gold_price_per_gram_thb:,.0f} THB")
st.write(f"**1 kg LBMA 99.99% gold =** {gold_price_per_gram_thb*1000:,.0f} THB")
st.write(f"**1 บาท 96.50% gold =** {gold_price_1baht_thb:,.0f} THB (by weight)")
