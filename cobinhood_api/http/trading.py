""" trading """
import time
import requests
from cobinhood_api.common import logger


class Trading(object):
    def __init__(self, config):
        self.token = config.API_TOKEN
        self.config = config
        self.BASE_URL = '%s/trading' % config.BASE_URL
        self.header = {
            'Authorization': self.token,
            'nonce': ''
        }

    @logger(obj=__name__)
    def get_trades(self, **parameter):
        """ /v1/trading/trades/:trade_id """
        self.header['nonce'] = str(int(float(time.time()) * 1000))
        para = '&'.join('{}={}'.format(k, v) for k, v in parameter.items())
        req = requests.get('%s/trades/?%s' % (self.BASE_URL, para),
                           headers=self.header)
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()

    @logger(obj=__name__)
    def post_orders(self, data):
        """ /v1/trading/orders """
        self.header['nonce'] = str(int(float(time.time()) * 1000))
        req = requests.post('%s/orders' % (self.BASE_URL),
                            json=data,
                            headers=self.header)
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()

    @logger(obj=__name__)
    def put_orders(self, order_id, data):
        """ /v1/trading/orders/:order_id """
        self.header['nonce'] = str(int(float(time.time()) * 1000))
        req = requests.put('%s/orders/%s' % (self.BASE_URL, order_id),
                           json=data,
                           headers=self.header)
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()

    @logger(obj=__name__)
    def get_orders(self, order_id=None, **parameter):
        """ /v1/trading/orders/:order_id """
        self.header['nonce'] = str(int(float(time.time()) * 1000))
        if order_id:
            req = requests.get('%s/orders/%s' % (self.BASE_URL, order_id),
                               headers=self.header)
        else:
            para = '&'.join('{}={}'.format(k, v) for k, v in parameter.items())
            req = requests.get('%s/orders?%s' % (self.BASE_URL, para),
                               headers=self.header)
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()

    @logger(obj=__name__)
    def delete_orders(self, order_id):
        """ /v1/trading/orders/:order_id """
        self.header['nonce'] = str(int(float(time.time()) * 1000))
        req = requests.delete('%s/orders/%s' % (self.BASE_URL, order_id),
                              headers=self.header)
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()

    @logger(obj=__name__)
    def get_order_history(self, **parameter):
        """ /v1/trading/order_history """
        self.header['nonce'] = str(int(float(time.time()) * 1000))
        para = '&'.join('{}={}'.format(k, v) for k, v in parameter.items())
        req = requests.get('%s/order_history/?%s' % (self.BASE_URL, para),
                           headers=self.header)
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()

    @logger(obj=__name__)
    def get_orders_trades(self, order_id):
        """ /v1/trading/orders/:order_id/trades """
        self.header['nonce'] = str(int(float(time.time()) * 1000))
        req = requests.get('%s/orders/%s/trades' % (self.BASE_URL, order_id),
                           headers=self.header)
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()
