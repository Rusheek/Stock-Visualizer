import pandas as pd
from utils import global_data as gd
import pandas_datareader.data as reader
from datetime import datetime, timedelta
import yfinance as yf

# yf.enable_debug_mode()

def load_data():
    url = 'https://en.wikipedia.org/wiki/NIFTY_50'
    df = pd.read_html(url)[1]
    df.rename(columns={df.columns[0]:"Company Name",df.columns[1]:"Ticker",df.columns[2]:"Sector",df.columns[3]:"Date Added"}, inplace=True)
    df['Ticker'] = df['Ticker'] + '.NS'
    gd.main_df = df
    gd.sectors_list = df['Sector'].unique()

def get_tickers_data(stocks_list,start_date,end_date):

    # tickers_df = yf.download(stocks_list,start_date,end_date)

    # df = reader.get_data_yahoo(stocks_list,start_date,end_date)
    # return df

    return yf.Tickers(stocks_list).download(start=start_date,end=end_date)

def test_functions(stock_list):
    x = yf.Tickers(stock_list)

    print (x.tickers['RELIANCE'].info)


end = datetime.now()
start = end - timedelta(days=365)

tickers = ['ADANIPORTS.NS','CIPLA.NS']
df = (get_tickers_data(tickers,start,end))
print(df[0])
