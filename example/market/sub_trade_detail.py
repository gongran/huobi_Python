from huobi.client.market import MarketClient
import os

os.environ["http_proxy"] = "http://127.0.0.1:10809"
os.environ["https_proxy"] = "http://127.0.0.1:10809"

def callback(trade_event: 'TradeDetailEvent'):
    print("---- trade_event:  ----")
    trade_event.print_object()
    print()



market_client = MarketClient(init_log=True)
market_client.sub_trade_detail("btcusdt", callback)

