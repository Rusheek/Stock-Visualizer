import streamlit as st
from utils import global_data as gd
from logic import graphs
import yfinance as yf
from datetime import datetime, timedelta
from plotly.subplots import make_subplots

st.write('Inside Index page')
index_list = ["Nifty50", "BankNifty"]
option = st.selectbox("Select the index from dropdown",index_list,index=None)
st.write("You have selected:", option)

if option is not None:
    index_ticker = gd.index_tickers[option]
    st.write("Ticker symbol for the index is :",index_ticker)
    #TODO add the code for displaying charts (Integration)
    # fetch the data of selected stock and display charts

    # Define date range (last 1 year)
    end = datetime.now()
    start = end - timedelta(days=365)

    # Download data in two shapes:
    # - df_multi: MultiIndex columns (required by interactive_candelsticks)
    # - df_single: single-level columns (required by mpf and RSI/candlestick helpers)
    df_multi = yf.download([index_ticker], start=start, end=end, auto_adjust=False)
    df_single = df_multi.copy()
    df_single.columns = df_single.columns.droplevel(1)

    # Optional: Peer line (module expects globals start/end)
    graphs.start = start
    graphs.end = end
    st.subheader("Peer Line")
    graphs.peer_line([index_ticker])

    # 1) Line chart
    st.subheader("Line Chart")
    graphs.Line_chart(df_single.reset_index())

    # 2) Interactive Candlesticks (expects MultiIndex-derived frame and a Date column)
    st.subheader("Interactive Candlestick")
    graphs.interactive_candelsticks(df_multi.reset_index())

    # 3) mplfinance plot
    st.subheader("MPF Candlestick with MAs & Volume")
    graphs.mpf_plots(df_single)

    # 4) Composite Plotly figure: Candlestick + Volume + RSI
    st.subheader("Candlestick + Volume + RSI")
    df_rsi = graphs.get_RSI(df_single.copy(), column='Adj Close', time_window=14)
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.03, row_heights=[0.55, 0.25, 0.20])
    graphs.plot_candlestick_chart(fig, df_single, row=1)
    graphs.plot_volume(fig, df_single, row=2)
    graphs.plot_RSI(fig, df_rsi, row=3)
    st.plotly_chart(fig, use_container_width=True)

    # 5) Bar plot (Volume)
    st.subheader("Volume Bar Plot")
    graphs.bar_plot(df_single[["Volume"]])
        
    