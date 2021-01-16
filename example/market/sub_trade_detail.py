import os

from huobi.client.market import MarketClient
from mysql.MyDB import MyDB

os.environ["http_proxy"] = "http://127.0.0.1:10809"
os.environ["https_proxy"] = "http://127.0.0.1:10809"

my_db = MyDB()


def callback(trade_event: 'TradeDetailEvent'):
    print("---- trade_event:  ----")
    objs = trade_event.print_object()
    my_db.insert_objs("trade", objs)
    print()


market_client = MarketClient(init_log=True)
market_client.sub_trade_detail("btcusdt", callback)
