from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import yfinance as yf
import streamlit as st
from PIL import Image
from urllib.request import urlopen

st.title("Crypto daily prices")
st.header("Crypto daily prices")

Bitcoin = 'BTC-USD'

BTC_Data = yf.Ticker(Bitcoin)

BTCHis = BTC_Data.history(period="max")
st.table(BTC)
st.bar_chart(BTCHis.Close)
