import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


aapl_df = yf.download('AAPL', start='2018-12-23', end='2023-12-23', progress=False,)
print(aapl_df.head())

msft_df = yf.download('MSFT', start='2018-12-23', end='2023-12-23', progress=False,)
print(msft_df.head())

goog_df = yf.download('GOOGL', start='2018-12-23', end='2023-12-23', progress=False,)
print(goog_df.head())

amzn_df = yf.download('AMZN', start='2018-12-23', end='2023-12-23', progress=False,)
print(amzn_df.head())


file_path1 = 'C:/Ashutosh/UG_22-26/WIDS_2023/apple.csv'
file_path2= 'C:/Ashutosh/UG_22-26/WIDS_2023/microsoft.csv'
file_path3 = 'C:/Ashutosh/UG_22-26/WIDS_2023/google.csv'
file_path4 = 'C:/Ashutosh/UG_22-26/WIDS_2023/amazon.csv'

aapl_df.to_csv(file_path1, index = True)
msft_df.to_csv(file_path2, index = True)
goog_df.to_csv(file_path3, index = True)
amzn_df.to_csv(file_path4, index = True)