""" chart """
import requests
from cobinhood.configuration import Config
from cobinhood.common import logger

BASE_URL = '%s/chart' % Config.BASE_URL


@logger(obj=__name__)
def get_candles(trading_pair_id):
    """ /v1/chart/candles/:trading_pair_id """
    req = requests.get('%s/candles/%s' % (BASE_URL, trading_pair_id))
    return req.json()
