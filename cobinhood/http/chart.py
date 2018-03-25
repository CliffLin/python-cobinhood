""" chart """
import requests
from cobinhood.configuration import Config
from cobinhood.common import logger

BASE_URL = '%s/chart' % Config.BASE_URL


class Chart(object):

    @logger(obj=__name__)
    def get_candles(self, trading_pair_id, **parameter):
        """ /v1/chart/candles/:trading_pair_id """
        para = '&'.join('{}={}'.format(k, v) for k, v in parameter.items())
        req = requests.get('%s/candles/%s?%s' % (BASE_URL,
                                                 trading_pair_id,
                                                 para))
        return req.json()
