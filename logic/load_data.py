import pandas as pd
from utils import global_data as gd

def load_data():
    url = 'https://en.wikipedia.org/wiki/NIFTY_50'
    df = pd.read_html(url)[1]
    print(df)
    
    

load_data()