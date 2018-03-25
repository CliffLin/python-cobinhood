""" system """
import requests
from cobinhood.configuration import Config
from cobinhood.common import logger

BASE_URL = '%s/system' % Config.BASE_URL


class System(object):

    @logger(obj=__name__)
    def get_version(self):
        """ /v1/system/version """
        req = requests.get('%s/version/' % (BASE_URL))
        return req.json()

    @logger(obj=__name__)
    def get_time(self):
        """ /v1/system/time """
        req = requests.get('%s/time/' % (BASE_URL))
        return req.json()

    @logger(obj=__name__)
    def get_messages(self, message_id=None):
        """ /v1/system/messages/:message_id """
        if message_id:
            req = requests.get('%s/messages/%s' % (BASE_URL, message_id))
        else:
            req = requests.get('%s/messages/' % (BASE_URL))
        return req.json()

    @logger(obj=__name__)
    def get_info(self):
        """ /v1/system/info """
        req = requests.get('%s/info/' % (BASE_URL))
        return req.json()
