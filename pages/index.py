import streamlit as st
from utils import global_data as gd

st.write('Inside Index page')
index_list = ["Nifty50", "BankNifty"]
option = st.selectbox("Select the index from dropdown",index_list,index=None)
st.write("You have selected:", option)

if option is not None:
    index_ticker = gd.index_tickers[option]
    st.write("Ticker symbol for the index is :",index_ticker)
    # TODO write logic to display charts
    