import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf

st.title("Stock Market Analysis")

start_date = st.date_input("Start Date", pd.to_datetime("2021-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("2022-01-01"))

ticker_symbol = st.text_input("Enter the symbol","AAPL")
Ticker_data = yf.Ticker(ticker_symbol)

Ticker_df = Ticker_data.history(start = start_date, end = end_date, period = '1d')

st.dataframe(Ticker_df)

st.write("Closing stock price charts")

clicked = st.button("Click me to see the stock related data")
if clicked:
    col1, _ = st.columns(2)

    with col1:
        st.write("## Daily closing price chart")
        st.line_chart(Ticker_df.Close)

    _, col2 = st.columns(2)
    with col1:
        st.write("## Daily volume chart")
        st.line_chart(Ticker_df.Volume)

clicked = st.button("Click me to see the random dataframe bar chart")
df = pd.DataFrame(np.random.rand(50,3), columns=['a','b','c'])
if clicked:
    st.write("You clicked")
    st.bar_chart(df)


