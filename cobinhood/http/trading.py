""" trading """
import time
import requests
from cobinhood.configuration import Config
from cobinhood.common import logger

BASE_URL = '%s/trading' % Config.BASE_URL


class Trading(object):
    def __init__(self, token=''):
        self.token = token
        self.header = {
            'Authorization': self.token,
            'nonce': ''
        }

    @logger(obj=__name__)
    def get_trades(self, **parameter):
        """ /v1/trading/trades/:trade_id """
        self.header['nonce'] = str(int(time.time()))
        para = '&'.join('{}={}'.format(k, v) for k, v in parameter.items())
        req = requests.get('%s/trades/?%s' % (BASE_URL, para),
                           headers=self.header)
        return req.json()

    @logger(obj=__name__)
    def post_orders(self, data):
        """ /v1/trading/orders """
        self.header['nonce'] = str(int(time.time()))
        req = requests.post('%s/orders/' % (BASE_URL),
                            json=data,
                            headers=self.header)
        return req.json()

    @logger(obj=__name__)
    def put_orders(self, order_id, data):
        """ /v1/trading/orders/:order_id """
        self.header['nonce'] = str(int(time.time()))
        req = requests.put('%s/orders/%s' % (BASE_URL, order_id), json=data,
                           headers=self.header)
        return req.json()

    @logger(obj=__name__)
    def get_orders(self, order_id=None):
        """ /v1/trading/orders/:order_id """
        self.header['nonce'] = str(int(time.time()))
        if order_id:
            req = requests.get('%s/orders/%s' % (BASE_URL, order_id),
                               headers=self.header)
        else:
            req = requests.get('%s/orders/' % (BASE_URL), headers=self.header)
        return req.json()

    @logger(obj=__name__)
    def delete_orders(self, order_id):
        """ /v1/trading/orders/:order_id """
        self.header['nonce'] = str(int(time.time()))
        req = requests.delete('%s/orders/%s' % (BASE_URL, order_id),
                              headers=self.header)
        return req.json()

    @logger(obj=__name__)
    def get_order_history(self, **parameter):
        """ /v1/trading/order_history """
        self.header['nonce'] = str(int(time.time()))
        para = '&'.join('{}={}'.format(k, v) for k, v in parameter.items())
        req = requests.get('%s/order_history/?%s' % (BASE_URL, para),
                           headers=self.header)
        return req.json()

    @logger(obj=__name__)
    def get_orders_trades(self, order_id):
        """ /v1/trading/orders/:order_id/trades """
        self.header['nonce'] = str(int(time.time()))
        req = requests.get('%s/orders/%s/trades' % (BASE_URL, order_id),
                           headers=self.header)
        return req.json()
