""" wallet """
import time
import requests
from cobinhood_api.configuration import Config
from cobinhood_api.common import logger


class Wallet(object):
    def __init__(self, config):
        self.token = config.API_TOKEN
        self.config = config
        self.BASE_URL = '%s/wallet' % config.BASE_URL
        self.headers = {
            'Authorization': self.token,
            'nonce': ''
        }

    @logger(obj=__name__)
    def get_deposits(self, deposit_id=None):
        """ /v1/wallet/deposits/:deposit_id """
        self.headers['nonce'] = str(int(float(time.time()) * 1000))
        if deposit_id:
            req = requests.get('%s/deposits/%s' % (self.BASE_URL, deposit_id),
                               headers=self.headers)
        else:
            req = requests.get('%s/deposits' % (self.BASE_URL),
                               headers=self.headers)
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()

    @logger(obj=__name__)
    def get_ledger(self, **parameter):
        """ /v1/wallet/ledger """
        self.headers['nonce'] = str(int(float(time.time()) * 1000))
        para = '&'.join('{}={}'.format(k, v) for k, v in parameter.items())
        req = requests.get('%s/ledger?%s' % (self.BASE_URL, para),
                           headers=self.headers)
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()

    @logger(obj=__name__)
    def getdeposit_addresses(self, **parameter):
        """ /v1/wallet/deposit_addresses """
        self.headers['nonce'] = str(int(float(time.time()) * 1000))
        para = '&'.join('{}={}'.format(k, v) for k, v in parameter.items())
        req = requests.get('%s/deposit_addresses?%s' % (self.BASE_URL, para),
                           headers=self.headers)
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()

    @logger(obj=__name__)
    def get_balances(self):
        """ /v1/wallet/balances """
        self.headers['nonce'] = str(int(float(time.time()) * 1000))
        req = requests.get('%s/balances' % (self.BASE_URL),
                           headers=self.headers)
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()

    @logger(obj=__name__)
    def get_withdrawals(self, withdrawal_id=None):
        """ /v1/wallet/withdrawals/:withdrawal_id """
        self.headers['nonce'] = str(int(float(time.time()) * 1000))
        if withdrawal_id:
            req = requests.get('%s/withdrawals/%s' % (self.BASE_URL,
                                                      withdrawal_id),
                               headers=self.headers)
        else:
            req = requests.get('%s/withdrawals' % (self.BASE_URL),
                               headers=self.headers)
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()

    @logger(obj=__name__)
    def get_limits_withdrawal(self):
        """ /v1/wallet/limits/withdrawal """
        self.headers['nonce'] = str(int(float(time.time()) * 1000))
        req = requests.get('%s/limits/withdrawal' % (self.BASE_URL),
                           headers=self.headers)
        if self.config.DEV:
            return req.json(), req.elapsed.total_seconds()
        return req.json()
