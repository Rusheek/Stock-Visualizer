import pandas as pd
from utils import global_data as gd
import pandas_datareader.data as reader
from datetime import datetime, timedelta
import yfinance as yf
import streamlit as st
import asyncio


# yf.enable_debug_mode()
# @st.cache_data
async def set_global_data():
    url = 'https://en.wikipedia.org/wiki/NIFTY_50'
    df = pd.read_html(url)[1]
    df.rename(columns={df.columns[0]:"Company Name",df.columns[1]:"Ticker",df.columns[2]:"Sector",df.columns[3]:"Date Added"}, inplace=True)
    df['Ticker'] = df['Ticker'] + '.NS'
    gd.nifty_df = df
    gd.sectors = df['Sector'].unique()

@st.cache_data
def get_tickers_technical_data(stocks_list,start_date,end_date):

    # tickers_df = yf.download(stocks_list,start_date,end_date)
    # df = reader.get_data_yahoo(stocks_list,start_date,end_date)
    # return df

    return yf.Tickers(stocks_list).download(start=start_date,end=end_date)

@st.cache_data
def get_tickers_fundamental_data(stocks_list,start_date,end_date):

    data = {}
    t = yf.Ticker(stocks_list)
    bs = t.get_balance_sheet(pretty=True,freq="quarterly")
    
    return bs

def test_functions(tickers):

    print (yf.Tickers(tickers).news)


# end = datetime.now()
# start = end - timedelta(days=365)

# tickers = 'ADANIPORTS.NS'
# df = (get_tickers_fundamental_data(tickers,start,end))
# print(df.iloc[:,0])

# test_functions(tickers)

