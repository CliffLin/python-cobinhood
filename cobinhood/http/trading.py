""" trading """
import time
import requests
from cobinhood.configuration import Config
from cobinhood.common import logger, Authorization

BASE_URL = '%s/trading' % Config.BASE_URL


@Authorization
@logger(obj=__name__)
def get_trades(trade_id=None):
    """ /v1/trading/trades/:trade_id """
    header = {'Authorization': Config.API_TOKEN,
              'nonce': str(int(time.time()))}
    if trade_id:
        req = requests.get('%s/trades/%s' % (BASE_URL, trade_id),
                           headers=header)
    else:
        req = requests.get('%s/trades/' % (BASE_URL), headers=header)
    return req.json()


@Authorization
@logger(obj=__name__)
def post_orders(data):
    """ /v1/trading/orders """
    header = {'Authorization': Config.API_TOKEN,
              'nonce': str(int(time.time()))}
    req = requests.post('%s/orders/' % (BASE_URL), json=data, headers=header)
    return req.json()


@Authorization
@logger(obj=__name__)
def put_orders(order_id, data):
    """ /v1/trading/orders/:order_id """
    time.sleep(1)
    header = {'Authorization': Config.API_TOKEN,
              'nonce': str(int(time.time()))}
    req = requests.put('%s/orders/%s' % (BASE_URL, order_id), json=data,
                       headers=header)
    return req.json()


@Authorization
@logger(obj=__name__)
def get_orders(order_id=None):
    """ /v1/trading/orders/:order_id """
    header = {'Authorization': Config.API_TOKEN,
              'nonce': str(int(time.time()))}
    if order_id:
        req = requests.get('%s/orders/%s' % (BASE_URL, order_id),
                           headers=header)
    else:
        req = requests.get('%s/orders/' % (BASE_URL), headers=header)
    return req.json()


@Authorization
@logger(obj=__name__)
def delete_orders(order_id):
    """ /v1/trading/orders/:order_id """
    time.sleep(0.5)
    header = {'Authorization': Config.API_TOKEN,
              'nonce': str(int(time.time()))}
    req = requests.delete('%s/orders/%s' % (BASE_URL, order_id),
                          headers=header)
    return req.json()


@Authorization
@logger(obj=__name__)
def get_order_history():
    """ /v1/trading/order_history """
    header = {'Authorization': Config.API_TOKEN,
              'nonce': str(int(time.time()))}
    req = requests.get('%s/order_history/' % (BASE_URL), headers=header)
    return req.json()


@Authorization
@logger(obj=__name__)
def get_orders_trades(order_id):
    """ /v1/trading/orders/:order_id/trades """
    header = {'Authorization': Config.API_TOKEN,
              'nonce': str(int(time.time()))}
    req = requests.get('%s/orders/%s/trades' % (BASE_URL, order_id),
                       headers=header)
    return req.json()
