#main.py
#Goldbartrading
import streamlit as st
from fetch import get_price, get_fx_to_thb

# App title
st.title("💰 Gold Bar Cal.")

# Fetch live data
gold_price_oz_usd = get_price("GC=F")
usd_to_thb = get_fx_to_thb("USD")

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

# 1. Troy oz
oz_qty = st.number_input("Quantity (troy oz)", min_value=0.0, value=1.0, step=0.01, key="oz_qty")
oz_total = gold_price_per_oz_thb * oz_qty
st.write(f"**{oz_qty:,.2f} troy oz of 99.99% gold =** {oz_total:,.0f} THB")

# 2. Gram
gram_qty = st.number_input("Quantity (gram)", min_value=0.0, value=1.0, step=1.0, key="gram_qty")
gram_total = gold_price_per_gram_thb * gram_qty
st.write(f"**{gram_qty:,.2f} gram of 99.99% gold =** {gram_total:,.0f} THB")

# 3. Thai baht weight
baht_qty = st.number_input("Quantity (บาท)", min_value=0.0, value=1.0, step=0.25, key="baht_qty")
baht_total = gold_price_1baht_thb * baht_qty
st.write(f"**{baht_qty:,.2f} บาท of 96.50% gold =** {baht_total:,.0f} THB (ไม่ใช่ราคาสมาคม)")
