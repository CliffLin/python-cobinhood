""" wallet """
import time
import requests
from cobinhood.configuration import Config
from cobinhood.common import logger

BASE_URL = '%s/wallet' % Config.BASE_URL


class Wallet(object):
    def __init__(self, token=''):
        self.token = token
        self.headers = {
            'Authorization': Config.API_TOKEN,
            'nonce': ''
        }

    @logger(obj=__name__)
    def get_deposits(self, deposit_id=None):
        """ /v1/wallet/deposits/:deposit_id """
        self.headers['nonce'] = str(int(time.time()))
        if deposit_id:
            req = requests.get('%s/deposits/%s' % (BASE_URL, deposit_id),
                               headers=self.headers)
        else:
            req = requests.get('%s/deposits/' % (BASE_URL),
                               headers=self.headers)
        return req.json()

    @logger(obj=__name__)
    def get_ledger(self, **parameter):
        """ /v1/wallet/ledger """
        self.headers['nonce'] = str(int(time.time()))
        para = '&'.join('{}={}'.format(k, v) for k, v in parameter.items())
        req = requests.get('%s/ledger?%s' % (BASE_URL, para),
                           headers=self.headers)
        return req.json()

    @logger(obj=__name__)
    def getdeposit_addresses(self, **parameter):
        """ /v1/wallet/deposit_addresses """
        self.headers['nonce'] = str(int(time.time()))
        para = '&'.join('{}={}'.format(k, v) for k, v in parameter.items())
        req = requests.get('%s/deposit_addresses?%s' % (BASE_URL, para),
                           headers=self.headers)
        return req.json()

    @logger(obj=__name__)
    def get_balances(self):
        """ /v1/wallet/balances """
        self.headers['nonce'] = str(int(time.time()))
        req = requests.get('%s/balances/' % (BASE_URL),
                           headers=self.headers)
        return req.json()

    @logger(obj=__name__)
    def get_withdrawals(self, withdrawal_id=None):
        """ /v1/wallet/withdrawals/:withdrawal_id """
        self.headers['nonce'] = str(int(time.time()))
        if withdrawal_id:
            req = requests.get('%s/withdrawals/%s' % (BASE_URL,
                                                      withdrawal_id),
                               headers=self.headers)
        else:
            req = requests.get('%s/withdrawals/' % (BASE_URL),
                               headers=self.headers)
        return req.json()

    @logger(obj=__name__)
    def get_limits_withdrawal(self):
        """ /v1/wallet/limits/withdrawal """
        self.headers['nonce'] = str(int(time.time()))
        req = requests.get('%s/limits/withdrawal/' % (BASE_URL),
                           headers=self.headers)
        return req.json()
