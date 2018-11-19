#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 10:48:05 2018

@author: Anneliese
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
yf.pdr_override()
import datetime
from scipy import stats

import warnings
warnings.filterwarnings("ignore")

# function to get the price data from yahoo finance
def getDataBatch(tickers, startdate, enddate):
  def getData(ticker):
    return (pdr.get_data_yahoo(ticker, start=startdate, end=enddate))
  datas = map(getData, tickers)
  return(pd.concat(datas, keys=tickers, names=['Ticker', 'Date']))

start_dt = datetime.datetime(2017, 7, 9)
end_dt = datetime.datetime(2018, 11, 18)

#----------------------------------------------
# get stock price from Yahoo Finance

# for multiple stock cases
tickers = ['AE-USD','ARDR-USD','BAT-USD','BCN-USD','BTC-USD','BTS-USD',
           'DASH-USD','DCR-USD','DGB-USD','DOGE-USD','EOS-USD','ETC-USD','ETH-USD','GNT-USD','IOT-USD','KMD-USD',
          'LSK-USD','LTC-USD','MAID-USD','MONA-USD','PIVX-USD','PPT-USD','QTUM-USD',
           'REP-USD','SC-USD','SNT-USD','STEEM-USD','STRAT-USD','USDT-USD','VEN-USD','WAVES-USD','XEM-USD',
           'XLM-USD','XMR-USD','XRP-USD','XVG-USD','ZEC-USD']
flag_download_data = False
if flag_download_data:
    price_data = getDataBatch(tickers, start_dt, end_dt)
   # Isolate the ‘Adj Close’ values and transform the DataFrame
    # Use Date as index and Ticker as column and only take the Adj_price values as contents
    daily_close_px = price_data.reset_index().pivot(index='Date', columns='Ticker', values='Adj Close')
    # modify the column name of S&P
    daily_close_px.rename(columns={'AE-USD','ARDR-USD','BAT-USD','BCN-USD','BTC-USD','BTS-USD',
           'DASH-USD','DCR-USD','DGB-USD','DOGE-USD','EOS-USD','ETC-USD','ETH-USD','GNT-USD','IOT-USD','KMD-USD',
          'LSK-USD','LTC-USD','MAID-USD','MONA-USD','PIVX-USD','PPT-USD','QTUM-USD',
           'REP-USD','SC-USD','SNT-USD','STEEM-USD','STRAT-USD','USDT-USD','VEN-USD','WAVES-USD','XEM-USD',
           'XLM-USD','XMR-USD','XRP-USD','XVG-USD','ZEC-USD'}, inplace=True)
    writer = pd.ExcelWriter('PriceData.xlsx', engine='xlsxwriter')
    daily_close_px.to_excel(writer, sheet_name='PriceData', startrow=1, startcol=0, header=True, index=True)
#else:
    #daily_close_px = pd.read_excel('PriceData2.xlsx', sheet_name='PriceData', header=0, index_col = 0)

try:
    price_data = getDataBatch(tickers, start_dt, end_dt)

    # Isolate the `Adj Close` values and transform the DataFrame
    # Use Date as index and Ticker as column and only take the Adj_price values as contents
    daily_close_px = price_data.reset_index().pivot(index='Date', columns='Ticker', values='Adj Close')
    writer = pd.ExcelWriter('PriceData.xlsx', engine='xlsxwriter')
    daily_close_px.to_excel(writer, sheet_name='PriceData', startrow=1, startcol=0, header=True, index=True)
    writer.save()

except:
    print('Uh-oh')
else:
    print("All good!  Imported and saved \n \n")
    
ret = daily_close_px.pct_change().dropna()
ret.columns = ['AE-USD','ARDR-USD','BAT-USD','BCN-USD','BTC-USD','BTS-USD',
           'DASH-USD','DCR-USD','DGB-USD','DOGE-USD','EOS-USD','ETC-USD','ETH-USD','GNT-USD','IOT-USD','KMD-USD',
          'LSK-USD','LTC-USD','MAID-USD','MONA-USD','PIVX-USD','PPT-USD','QTUM-USD',
           'REP-USD','SC-USD','SNT-USD','STEEM-USD','STRAT-USD','USDT-USD','VEN-USD','WAVES-USD','XEM-USD',
           'XLM-USD','XMR-USD','XRP-USD','XVG-USD','ZEC-USD']


    
    

