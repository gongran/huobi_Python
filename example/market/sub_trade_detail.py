import os

from huobi.client.market import MarketClient
from mysql.MyDB import MyDB

os.environ["http_proxy"] = "http://127.0.0.1:10809"
os.environ["https_proxy"] = "http://127.0.0.1:10809"

my_db = MyDB()
symbols = "btcusdt"


def add_coin_type(ob, ch):
    ob['coin_type'] = ch
    return ob


def callback(trade_event: 'TradeDetailEvent'):
    objs = trade_event.print_object()
    objs = list(map(lambda ob: add_coin_type(ob, trade_event.ch), objs))
    my_db.insert_objs("trade", objs)


market_client = MarketClient(init_log=True)
market_client.sub_trade_detail(symbols, callback)
