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
    st.line_chart(history['Close'])
    st.write(f"Name: {info.get('longName', 'N/A')}")
    st.write(f"Current Price: ₹{info.get('currentPrice', 'N/A')}")
    st.write(f"Market Cap: ₹{info.get('marketCap', 'N/A')}")
    st.write(f"PE Ratio: {info.get('trailingPE', 'N/A')}")
    st.write(f"Day High: ₹{info.get('dayHigh', 'N/A')}")
    st.write(f"Day Low: ₹{info.get('dayLow', 'N/A')}")
    st.write(f"52 Week High: ₹{info.get('fiftyTwoWeekHigh', 'N/A')}")
    st.write(f"52 Week Low: ₹{info.get('fiftyTwoWeekLow', 'N/A')}")
    
period = st.selectbox("Select Time Period", ["1d", "5d", "1mo", "3mo", "6mo", "1y"])
history = stock.history(period=period)
st.line_chart(history['Close'])

    

