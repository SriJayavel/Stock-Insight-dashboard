import streamlit as st
import yfinance as yf

st.title("Stock Insight Dashboard")
ticker = "RELIANCE.NS"
stock = yf.Ticker(ticker)
info = stock.info
st.subheader("Company Information")
st.write(f"Name: {info.get('longName', 'N/A')}")
st.write(f"Current Price: ₹{info.get('currentPrice', 'N/A')}")
tricker = st.text_input("Enter Stock Ticker", value="RELIANCE.NS")