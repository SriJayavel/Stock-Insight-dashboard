import streamlit as st
import yfinance as yf
import pandas as pd
companies = pd.read_csv("companies.csv")

# Set page configuration
st.set_page_config(page_title="Stock Insight Dashboard", layout="wide")
st.title("Stock Insight Dashboard")
st.caption("Built by Jay")

#Search functionality
search = st.text_input("Search Company Name")

info = None
ticker = None
matches = pd.DataFrame()

if search and len(search) >= 2:
    matches = companies[
        companies["NAME OF COMPANY"].str.contains(search, case=False, na=False)
        | 
        companies["SYMBOL"].str.contains(search, case=False, na=False)
    ]

    if not matches.empty:
       selected_company = st.selectbox("Select a Company",matches["NAME OF COMPANY"].head(10)
    )
       selected_row = matches[matches["NAME OF COMPANY"] == selected_company].iloc[0]
       ticker = selected_row["SYMBOL"] + ".NS"
    else:
        st.warning("No matching companies found.")
elif search:
     st.warning("Please enter at least 2 characters to search.")

 
 #Display stock price history and key metrics
if ticker:
     stock = yf.Ticker(ticker)
     info = stock.info
     st.metric("Company Name", info.get('longName', 'N/A'))     
     st.subheader("Stock Price History")
     period = st.selectbox("Select Time Period", ["1d", "5d", "1mo", "3mo", "6mo", "1y"])
     history = stock.history(period=period)
     st.line_chart(history['Close'])
     market_cap = info.get('marketCap', 0)

     # Display company overview
     st.subheader("Company Information")
     st.write(f"Sector: {info.get('sector', 'N/A')}")
     st.write(f"Industry: {info.get('industry', 'N/A')}")
     st.write(f"Description: {info.get('longBusinessSummary', 'N/A')}") 
# Format market cap for better readability
     if market_cap >= 1_000_000_000_000:
         value = f"{market_cap / 1_000_000_000_000:.2f} Trillion"
     elif market_cap >= 1_000_000_000:
         value = f"{market_cap / 1_000_000_000:.2f} Billion" 
     elif market_cap >= 1_000_000:
         value = f"{market_cap / 1_000_000:.2f} Million"
     else:
         value = f"{market_cap}"

     st.subheader("Key Metrics")
     col1, col2, col3 = st.columns(3)
     with col1:
         st.metric("Current Price", f"₹{info.get('currentPrice', 'N/A')}")
         st.metric("Market Cap", f"₹{value}")
     with col2:
         st.metric("Day High", f"₹{info.get('dayHigh', 'N/A')}")
         st.metric("Day Low", f"₹{info.get('dayLow', 'N/A')}") 
     with col3:
         st.metric("PE Ratio", f"{pe_ratio:.2f}" if (pe_ratio := info.get('trailingPE')) is not None else "N/A")
         st.metric("52 Week High", f"₹{info.get('fiftyTwoWeekHigh', 'N/A')}")
         st.metric("52 Week Low", f"₹{info.get('fiftyTwoWeekLow', 'N/A')}") 
 
#STOCK COMPARISON

st.header("Stock Comparison")
st.caption("Select multiple Indian stocks over the past year.")
comparison_options = sorted(companies["NAME OF COMPANY"].dropna().unique().tolist())
selected_companies = st.multiselect("Select Companies to Compare", options=comparison_options, default=comparison_options[:2])

if selected_companies:
    selected_tickers = []
    for company in selected_companies:
        row = companies[companies["NAME OF COMPANY"] == company]
        if not row.empty:
            ticker_symbol = row.iloc[0]["SYMBOL"] + ".NS"
            selected_tickers.append(ticker_symbol)

    if selected_tickers:
        comparison_data = yf.download(selected_tickers, period="1y")['Close']
        st.line_chart(comparison_data)
    else:
        st.warning("No valid tickers found for the selected companies.")

#Investment Return Calculator
investment_return_calculator = st.sidebar.expander("Investment Return Calculator")
with investment_return_calculator:
    st.subheader("Calculate Investment Returns")
    initial_investment = st.number_input("Initial Investment (₹)", min_value=0.0, value=10000.0)
    annual_return_rate = st.number_input("Expected Annual Return Rate (%)", min_value=0.0, value=10.0)
    investment_duration = st.number_input("Investment Duration (Years)", min_value=1, value=5)
    if st.button("Calculate"):
        future_value = initial_investment * ((1 + annual_return_rate / 100) ** investment_duration)
        st.write(f"Future Value of Investment: ₹{future_value:,.2f}")
        effective_annual_return = ((future_value / initial_investment) ** (1 / investment_duration) - 1) * 100
        st.write(f"Effective Annual Return: {effective_annual_return:.2f}%")
    else:
        st.write("Enter the details and click 'Calculate' to see the results.")




    

