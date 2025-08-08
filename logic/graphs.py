# Logic for all the graphs
import streamlit as st
import pandas_datareader.data as reader
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import mplfinance as mpf
import yfinance as yf

#Peer_Line
def relativeret(df):
    daily_returns = df.pct_change()
    daily_cum_returns = (daily_returns +1).cumprod()
    daily_cum_returns = daily_cum_returns.fillna(0)
    return daily_cum_returns

def peer_line(sts):
    dropdown = st.multiselect('Pick your assest',sts)
    if len(dropdown)>0:
        df = yf.download(dropdown, start, end, auto_adjust=False)
        
        df = relativeret(df['Adj Close'])
        # st.write(df)
        i=0
        fig = go.Figure()
        st.write(dropdown)
        for x in dropdown:
            fig.add_trace(go.Scatter(x=df.index,y=df[x],mode ='lines',name=x))

        st.plotly_chart(fig)

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


#mpf_plots
def mpf_plots(df):
    
    fig, axes = mpf.plot(
        df,
        type='candle',
        style='yahoo',
        title='Moving Averages',
        ylabel='Price',
        ylabel_lower='Volume',
        volume=True,
        mav=(50, 200),
        tight_layout=True,
        figscale=0.75,
        returnfig=True  
    )
    
    
    st.pyplot(fig)

#RSI
def get_RSI(df, column='Adj Close', time_window=14):
    """Return the RSI indicator for the specified time window."""
    diff = df[column].diff(1)

    # This preservers dimensions off diff values.
    up_chg = 0 * diff
    down_chg = 0 * diff

    # Up change is equal to the positive difference, otherwise equal to zero.
    up_chg[diff > 0] = diff[diff > 0]

    # Down change is equal to negative deifference, otherwise equal to zero.
    down_chg[diff < 0] = diff[diff < 0]

    # We set com = time_window-1 so we get decay alpha=1/time_window.
    up_chg_avg = up_chg.ewm(com=time_window - 1,
                            min_periods=time_window).mean()
    down_chg_avg = down_chg.ewm(com=time_window - 1,
                                min_periods=time_window).mean()

    RS = abs(up_chg_avg / down_chg_avg)
    df['RSI'] = 100 - 100 / (1 + RS)

    return df


def plot_volume(fig, df, row, column=1):
    """Return a graph object figure containing the volume chart in the specified row."""
    fig.add_trace(go.Bar(x=df.index,
                         y=df['Volume'],
                         marker=dict(color='lightskyblue',
                                     line=dict(color='firebrick', width=0.1)),
                         showlegend=False,
                         name='Volume'),
                  row=row,
                  col=column)

    fig.update_xaxes(title_text='Date', row=row, col=column)
    fig.update_yaxes(title_text='Volume ', row=row, col=column)

    return fig


def plot_RSI(fig, df, row, column=1):
    """Return a graph object figure containing the RSI indicator in the specified row."""
    df1=df.reset_index()
    fig.add_trace(go.Scatter(x=df1['Date'].iloc[30:],
                             y=df1['RSI'].iloc[30:],
                             name='RSI',
                             line=dict(color='gold', width=2)),
                  row=row,
                  col=column)

    fig.update_yaxes(title_text='RSI', row=row, col=column)

    # Add one red horizontal line at 70% (overvalued) and green line at 30% (undervalued)
    for y_pos, color in zip([70, 30], ['Red', 'Green']):
        fig.add_shape(x0=df1['Date'].iloc[1],
                      x1=df1['Date'].iloc[-1],
                      y0=y_pos,
                      y1=y_pos,
                      type='line',
                      line=dict(color=color, width=2),
                      row=row,
                      col=column)

    # Add a text box for each line
    for y_pos, text, color in zip([64, 36], ['Overvalued', 'Undervalued'], ['Red', 'Green']):
        fig.add_annotation(x=df1['Date'].iloc[int(df1['Date'].shape[0] / 10)],
                           y=y_pos,
                           text=text,
                           font=dict(size=14, color=color),
                           bordercolor=color,
                           borderwidth=1,
                           borderpad=2,
                           bgcolor='lightsteelblue',
                           opacity=0.75,
                           showarrow=False,
                           row=row,
                           col=column)

    # Update the y-axis limits
    ymin = 25 if df1['RSI'].iloc[30:].min() > 25 else df1['RSI'].iloc[30:].min() - 5
    ymax = 75 if df1['RSI'].iloc[30:].max() < 75 else df1['RSI'].iloc[30:].max() + 5
    fig.update_yaxes(range=[ymin, ymax], row=row, col=column)

    return fig


def plot_candlestick_chart(fig, df, row, column=1):
    """Return a graph object figure containing a Candlestick chart in the specified row."""
    fig.add_trace(go.Candlestick(x=df.index,
                                 open=df['Open'],
                                 high=df['High'],
                                 low=df['Low'],
                                 close=df['Close'],
                                 name='Candlestick Chart'),
                  row=row,
                  col=column)
    fig.update_xaxes(rangeslider={'visible': False})
    fig.update_yaxes(title_text='Price ', row=row, col=column)

    return fig

def bar_plot(df):
    st.bar_chart(df)
