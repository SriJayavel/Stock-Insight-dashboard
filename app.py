import streamlit as st
import yfinance as yf

st.title("Stock Insight Dashboard")
ticker = "RELIANCE.NS"
stock = yf.Ticker(ticker)
info = stock.info
st.subheader("Company Information")
st.write(f"Name: {info.get('longName', 'N/A')}")
st.write(f"Current Price: ₹{info.get('currentPrice', 'N/A')}")
ticker = st.text_input("Enter Stock Symbol", value="RELIANCE")
ticker = ticker.upper() + ".NS"
info.get('Current Price', 'N/A')
if ticker:
    stock = yf.Ticker(ticker)
    info = stock.info
    st.subheader("Company Information")
    history = stock.history(period="1y")
    period = st.selectbox("Select Time Period", ["1d", "5d", "1mo", "3mo", "6mo", "1y"])
    history = stock.history(period=period)
    st.line_chart(history['Close'])
    st.metric("Name", info.get('longName', 'N/A'))
    st.metric("Current Price", f"₹{info.get('currentPrice', 'N/A')}")
    st.metric("Market Cap", f"₹{info.get('marketCap', 'N/A')}")
    st.metric("PE Ratio", info.get('trailingPE', 'N/A'))
    st.metric("Day High", f"₹{info.get('dayHigh', 'N/A')}")
    st.metric("Day Low", f"₹{info.get('dayLow', 'N/A')}")
    st.metric("52 Week High", f"₹{info.get('fiftyTwoWeekHigh', 'N/A')}")
    st.metric("52 Week Low", f"₹{info.get('fiftyTwoWeekLow', 'N/A')}") 
    

    

