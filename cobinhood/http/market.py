""" market """
import requests
from cobinhood.configuration import Config
from cobinhood.common import logger

BASE_URL = '%s/market' % Config.BASE_URL


@logger(obj=__name__)
def get_trades(trading_pair_id):
    """ /v1/market/trades/:trading_pair_id """
    req = requests.get('%s/trades/%s' % (BASE_URL, trading_pair_id))
    return req.json()


@logger(obj=__name__)
def get_stats():
    """ /v1/market/stats """
    req = requests.get('%s/stats/' % (BASE_URL))
    return req.json()


@logger(obj=__name__)
def get_currency_intro():
    """ /v1/market/currency_intro """
    req = requests.get('%s/currency_intro/' % (BASE_URL))
    return req.json()


@logger(obj=__name__)
def get_tickers(trading_pair_id):
    """ /v1/market/tickers/:trading_pair_id """
    req = requests.get('%s/tickers/%s' % (BASE_URL, trading_pair_id))
    return req.json()


@logger(obj=__name__)
def get_exchange_rates(currency_id):
    """ /v1/market/exchange_rates/:currency_id """
    req = requests.get('%s/exchange_rates/%s' % (BASE_URL, currency_id))
    return req.json()


@logger(obj=__name__)
def get_orderbooks(trading_pair_id):
    """ /v1/market/orderbooks/:trading_pair_id """
    req = requests.get('%s/orderbooks/%s' % (BASE_URL, trading_pair_id))
    return req.json()


@logger(obj=__name__)
def get_orderbook_precisions(trading_pair_id):
    """ /v1/market/orderbook/precisions/:trading_pair_id """
    req = requests.get('%s/orderbook/precisions/%s' % (BASE_URL,
                                                       trading_pair_id))
    return req.json()


@logger(obj=__name__)
def get_currencies():
    """ /v1/market/currencies """
    req = requests.get('%s/currencies/' % (BASE_URL))
    return req.json()


@logger(obj=__name__)
def get_trading_pairs():
    """ /v1/market/trading_pairs """
    req = requests.get('%s/trading_pairs/' % (BASE_URL))
    return req.json()
