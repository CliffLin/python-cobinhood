""" system """
import requests
from cobinhood_api.common import logger


class System(object):
    def __init__(self, config):
        self.config = config
        self.BASE_URL = '%s/system' % config.BASE_URL

    @logger(obj=__name__)
    def get_version(self):
        """ /v1/system/version """
        req = requests.get('%s/version' % (self.BASE_URL))
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()

    @logger(obj=__name__)
    def get_time(self):
        """ /v1/system/time """
        req = requests.get('%s/time' % (self.BASE_URL))
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()

    @logger(obj=__name__)
    def get_messages(self, message_id=None):
        """ /v1/system/messages/:message_id """
        if message_id:
            req = requests.get('%s/messages/%s' % (self.BASE_URL, message_id))
        else:
            req = requests.get('%s/messages' % (self.BASE_URL))
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()

    @logger(obj=__name__)
    def get_info(self):
        """ /v1/system/info """
        req = requests.get('%s/info' % (self.BASE_URL))
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()
