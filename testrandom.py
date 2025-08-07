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

def interactive_candelsticks(df):
    # if not isinstance(df.index, pd.DatetimeIndex):
    #     df['Date'] = pd.to_datetime(df['Date'])
    # else:
    #     df['Date'] = df.index

    df.reset_index(inplace=True)
    # df.dropna(subset=['Open', 'High', 'Low', 'Close'], inplace=True)

    fig = go.Figure(data =[go.Candlestick(x=df['Date'],
                                    open = df['Open'],
                                    high = df['High'],
                                    low = df['Low'],
                                    close = df['Close'],
                                    increasing_line_color = 'green',
                                    decreasing_line_color = 'red')])
 
    fig.update_layout(
        title="Candlestick Chart",
        xaxis_title="Date",
        yaxis_title="Price",
        xaxis_rangeslider_visible=False
    )
    st.write(df)
    st.write(df['Date'])
    st.write(df['Open'])
    # print(df[['Open', 'High', 'Low', 'Close']].dtypes)

    st.plotly_chart(fig, use_container_width=True)

start = dt.date(2019,5,1)
end = dt.datetime.now()

sample_data = pd.DataFrame({
    'Date': pd.to_datetime([
        '2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'
    ]),
    'Open':  [100, 102, 101, 105, 107],
    'High':  [105, 106, 104, 108, 110],
    'Low':   [99, 100, 98, 103, 105],
    'Close': [103, 101, 102, 107, 109]
})

# Set date as index if your function expects that
sample_data.set_index('Date', inplace=True)

Data = yf.download("AAPL", start=start, end=end)
# Data = Data.iloc[1:]
# titles = ['Open','High','Low','Close', 'Volume' ]
# ndf = ndf[titles]
# ndf1 = ndf['Close']
Data.reset_index(inplace=True)
st.line_chart(Data.set_index("Date")["Close"])
if Data.empty:
    st.error("NO DATA!")
interactive_candelsticks(Data)