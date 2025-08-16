from datetime import datetime, timedelta

nifty_df = None
sectors = []
index_tickers = {'Nifty50' :'^NSEI', 'BankNifty':'^NSEBANK'}

end = datetime.now()
start = end - timedelta(days=365)