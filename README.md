## Cobinhood API 
### Install
`pip install git+https://github.com/CliffLin/python-cobinhood`
### Usage
<b>Basic Usage</b>
<pre>
from cobinhood.http import system
print system.get_time()
</pre>

**Private Token Usage**
<pre>
from cobinhood.configuration import Config
from cobinhood.http import wallet
Config.API_TOKEN = 'YOUR_API_TOKEN'
print wallet.get_balances()
</pre>

**Websocket Usgae**
<pre>
from cobinhood.ws import feed
from cobinhood.ws.subscribe import Orderbook

def on_message(ws_obj, msg):
    print ws_obj.exchange_data.orderbook
    print msg

ws = feed.CobinhoodWS()
cobeth_orderbook = Orderbook('COB-ETH')
ws.start(subscribe=[cobeth_orderbook], on_message=on_message)

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
cobinhood.http.trade.post_order(data)
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
