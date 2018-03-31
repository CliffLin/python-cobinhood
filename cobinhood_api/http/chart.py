""" chart """
import requests
from cobinhood_api.common import logger


class Chart(object):
    def __init__(self, config):
        self.config = config
        self.BASE_URL = '%s/chart' % config.BASE_URL

    @logger(obj=__name__)
    def get_candles(self, trading_pair_id, **parameter):
        """ /v1/chart/candles/:trading_pair_id """
        para = '&'.join('{}={}'.format(k, v) for k, v in parameter.items())
        req = requests.get('%s/candles/%s?%s' % (self.BASE_URL,
                                                 trading_pair_id,
                                                 para))
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()
