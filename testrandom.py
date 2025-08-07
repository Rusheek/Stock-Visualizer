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

    # st.write(df.set_index("Date")["Close"])
    df.reset_index(inplace=True)

    st.line_chart(df.set_index("Date")["Close"])

def interactive_candelsticks(df):
                  
    df.set_index('Date', inplace=True)
    # st.write(df)
    # st.write(df.columns)
    df.columns = df.columns.droplevel(1)

    # st.write(df.columns)
    df = df.reset_index()

    # st.write(df)

    fig = go.Figure(data =[go.Candlestick(x=df['Date'],
                                     open=df['Open'],
                                     high = df['High'],
                                     low = df['Low'],
                                     close = df['Close'])])

    # st.plotly_chart(fig)

    # Layout customization
    fig.update_layout(
        title="Nifty 50 Index (Candlestick)",
        xaxis_title="Date",
        yaxis_title="Price (INR)",
        xaxis_rangeslider_visible=False,
        template="plotly_dark",
        height=600
    )

    # Display in Streamlit
    st.plotly_chart(fig, use_container_width=True)

start = dt.date(2024,5,1)
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

sample_data.set_index('Date', inplace=True)

Data = yf.download("^NSEI", start=start, end=end,interval="1d")

Line_chart(Data)

interactive_candelsticks(Data)