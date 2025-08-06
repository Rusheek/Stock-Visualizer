import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas_datareader.data as reader
import datetime as dt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
import plotly.express as px
import yfinance as yf


def Line_chart(df):
    st.line_chart(df.set_index("Date")["Close"])

start = dt.date(2019,5,1)
end = dt.datetime.now()

data = yf.download("^NSEI", start=start, end=end)
# titles = ['Open','High','Low','Close', 'Volume' ]
# ndf = ndf[titles]
# ndf1 = ndf['Close']
data.reset_index(inplace=True)
st.line_chart(data.set_index("Date")["Close"])