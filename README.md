## Cobinhood API 
### Install
`pip install git+https://github.com/CliffLin/python-cobinhood`
### Usage
<b>Basic Usage</b>
<pre>
from cobinhood_api import Cobinhood
cob = Cobinhood()
print cob.system.get_time()
</pre>

**Private Token Usage**
<pre>
from cobinhood_api import Cobinhood
cob = Cobinhood(API_TOKEN='YOUR_API_TOKEN')
print cob.wallet.get_balances()
</pre>

**Websocket Usgae**
<pre>
from cobinhood_api import Cobinhood
from cobinhood_api.ws.subscribe import Orderbook

def on_message(cob_obj, msg):
    print cob_obj.system.get_time()
    print cob_obj.ws.exchange_data.orderbook
    print msg

cob = Cobinhood()
cobeth_orderbook = Orderbook('COB-ETH')
cob.ws.start(subscribe=[cobeth_orderbook], on_message=on_message)

</pre>

## Data Format
### API Return
REST API will return a `dict` 
ex: 
<pre>
# return of cobinhood.http.system.get_time()
{'result': {'time': 1520344325656}, 'success': True}
</pre>
### API Post or Put Data
You need to post `dict` data to api function
ex:
<pre>
# place order
data = {
    "trading_pair_id": "BTC-USDT",
    "side": "bid",
    "type": "limit",
    "price": "5000.01000000",
    "size": "1.0100"
}
cobinhood.trade.post_order(data)
</pre>
### Websocket response
You need to design a callback function with two parameters: CobinhoodWS object, response message(json).  
You can handle the response youself with response message, or you can use CobinhoodWS.exchange_data to get the *fancy* object like below:
<pre>
CobinhoodWS.exchange_data.orderbook = {
    'COB-ETH': {
        '1E-7': CobinhoodWS.Orderbook(object),
        '1E-6': CobinhoodWS.Orderbook(object)
    }  
}
CobinhoodWS.exchange_data.ticker = {
    'COB-ETH': CobinhoodWS.Ticker(object)
}
</pre>
## API Endpoint  
### cobinhood.candle
* /v1/chart/candles/:trading_pair_id  
  `get_candles(trading_pair_id)`
### cobinhood.market
* /v1/market/trades/:trading_pair_id  
  `get_trades(trading_pair_id)`
* /v1/market/stats  
  `get_stats()`
* /v1/market/currency_intro  
  `get_currency_intro()`
* /v1/market/tickers/:trading_pair_id  
  `get_tickers(trading_pair_id)`
* /v1/market/exchange_rates/:currency_id  
  `get_exchange_rates(currency_id)`
* /v1/market/orderbooks/:trading_pair_id  
  `get_orderbooks(trading_pair_id)`
* /v1/market/orderbook/precisions/:trading_pair_id  
  `get_orderbook_precisions(trading_pair_id)`
* /v1/market/currencies  
  `get_currencies()`
* /v1/market/trading_pairs  
  `get_trading_pairs()`
### cobinhood.system
* /v1/system/version  
  `get_version()`
* /v1/system/time  
  `get_time()`
* /v1/system/messages/:message_id  
  `get_messages(message_id=None)`
* /v1/system/info  
  `get_info()`
### cobinhood.trading
* /v1/trading/trades/:trade_id  
  `get_trades(trade_id=None)`
* /v1/trading/orders  
  `post_orders(data)`
* /v1/trading/orders/:order_id  
  `put_orders(order_id, data)`
* /v1/trading/orders/:order_id  
  `get_orders(order_id=None)`
* /v1/trading/orders/:order_id  
  `delete_orders(order_id)`
* /v1/trading/order_history  
  `get_order_history()`
* /v1/trading/orders/:order_id/trades  
  `get_orders_trades(order_id)`
### cobinhood.wallet
* /v1/wallet/deposits/:deposit_id  
  `get_deposits(deposit_id=None)`
* /v1/wallet/ledger  
  `get_ledger()`
* /v1/wallet/withdrawal_addresses  
  `get_withdrawal_addresses()`
* /v1/wallet/deposit_addresses  
  `get_deposit_addresses()`
* /v1/wallet/balances  
  `get_balances()`
* /v1/wallet/withdrawals/:withdrawal_id  
  `get_withdrawals(withdrawal_id=None)`
* /v1/wallet/limits/withdrawal  
  `get_limits_withdrawal()`
## Websocket Topic
* `cobinhood_api.ws.subscribe.Trade(trading_pair_id)`
* `cobinhood_api.ws.subscribe.Orderbook(trading_pair_id, precision=None)`
* `cobinhood_api.ws.subscribe.Ticker(trading_pair_id)`
* `cobinhood_api.ws.subscribe.Candle(trading_pair_id, precision=None)`
* `cobinhood_api.ws.subscribe.Order()`
