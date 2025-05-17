import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np


st.title("Hello Streamlit")
st.write("This is my first streamlit application")

df = pd.DataFrame({"A":[1,2,3], "B": [4,5,6]})
st.table(df)

df = pd.DataFrame(np.random.rand(50,3), columns = ['a','b','c'])
st.line_chart(df)

name = st.text_input('Enter Your Name')
age = st.slider('age', 10,20,30)
agree = st.checkbox("I agree")
choice = st.selectbox("Pick one", ['Option1','Option2','Option3'])
if st.button('Say Hello'):
    st.write(f"Hello {name}")

col1, col2 = st.columns(2)
with col1:
    st.write("Left Column")
with col2:
    st.write("Right column")