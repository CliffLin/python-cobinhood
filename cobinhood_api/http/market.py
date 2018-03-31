""" market """
import requests
from cobinhood_api.common import logger


class Market(object):
    def __init__(self, config):
        self.config = config
        self.BASE_URL = '%s/market' % config.BASE_URL

    @logger(obj=__name__)
    def get_trades(self, trading_pair_id, **parameter):
        """ /v1/market/trades/:trading_pair_id """
        para = '&'.join('{}={}'.format(k, v) for k, v in parameter.items())
        req = requests.get('%s/trades/%s?%s' % (self.BASE_URL,
                                                trading_pair_id,
                                                para))
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()

    @logger(obj=__name__)
    def get_stats(self):
        """ /v1/market/stats """
        req = requests.get('%s/stats' % (self.BASE_URL))
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()

    @logger(obj=__name__)
    def get_currency_intro(self, **parameter):
        """ /v1/market/currency_intro """
        para = '&'.join('{}={}'.format(k, v) for k, v in parameter.items())
        req = requests.get('%s/currency_intro?%s' % (self.BASE_URL, para))
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()

    @logger(obj=__name__)
    def get_tickers(self, trading_pair_id=""):
        """ /v1/market/tickers/:trading_pair_id """
        req = requests.get('%s/tickers/%s' % (self.BASE_URL, trading_pair_id))
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()

    @logger(obj=__name__)
    def get_exchange_rates(self, currency_id):
        """ /v1/market/exchange_rates/:currency_id """
        req = requests.get('%s/exchange_rates/%s' % (self.BASE_URL,
                                                     currency_id))
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()

    @logger(obj=__name__)
    def get_orderbooks(self, trading_pair_id, **parameter):
        """ /v1/market/orderbooks/:trading_pair_id """
        para = '&'.join('{}={}'.format(k, v) for k, v in parameter.items())
        req = requests.get('%s/orderbooks/%s?%s' % (self.BASE_URL,
                                                    trading_pair_id,
                                                    para))
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()

    @logger(obj=__name__)
    def get_orderbook_precisions(self, trading_pair_id):
        """ /v1/market/orderbook/precisions/:trading_pair_id """
        req = requests.get('%s/orderbook/precisions/%s' % (self.BASE_URL,
                                                           trading_pair_id))
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()

    @logger(obj=__name__)
    def get_currencies(self):
        """ /v1/market/currencies """
        req = requests.get('%s/currencies' % (self.BASE_URL))
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()

    @logger(obj=__name__)
    def get_trading_pairs(self):
        """ /v1/market/trading_pairs """
        req = requests.get('%s/trading_pairs' % (self.BASE_URL))
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()
