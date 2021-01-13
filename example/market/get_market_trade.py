from huobi.client.market import MarketClient
from huobi.utils import *
import os

os.environ["http_proxy"] = "http://127.0.0.1:10809"
os.environ["https_proxy"] = "http://127.0.0.1:10809"
market_client = MarketClient()
list_obj = market_client.get_market_trade(symbol="btcusdt")
LogInfo.output_list(list_obj)
