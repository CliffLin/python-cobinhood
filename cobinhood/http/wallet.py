""" wallet """
import time
import requests
from cobinhood.configuration import Config
from cobinhood.common import logger, Authorization

BASE_URL = '%s/wallet' % Config.BASE_URL


@Authorization
@logger(obj=__name__)
def get_deposits(deposit_id=None):
    """ /v1/wallet/deposits/:deposit_id """
    header = {'Authorization': Config.API_TOKEN,
              'nonce': str(int(time.time()))}
    if deposit_id:
        req = requests.get('%s/deposits/%s' % (BASE_URL, deposit_id),
                           headers=header)
    else:
        req = requests.get('%s/deposits/' % (BASE_URL), headers=header)
    return req.json()


@Authorization
@logger(obj=__name__)
def get_ledger():
    """ /v1/wallet/ledger """
    header = {'Authorization': Config.API_TOKEN,
              'nonce': str(int(time.time()))}
    req = requests.get('%s/ledger/' % (BASE_URL), headers=header)
    return req.json()


@Authorization
@logger(obj=__name__)
def get_withdrawal_addresses():
    """ /v1/wallet/withdrawal_addresses """
    header = {'Authorization': Config.API_TOKEN,
              'nonce': str(int(time.time()))}
    req = requests.get('%s/withdrawal_addresses/' % (BASE_URL), headers=header)
    return req.json()


@Authorization
@logger(obj=__name__)
def get_deposit_addresses():
    """ /v1/wallet/deposit_addresses """
    header = {'Authorization': Config.API_TOKEN,
              'nonce': str(int(time.time()))}
    req = requests.get('%s/deposit_addresses/' % (BASE_URL), headers=header)
    return req.json()


@Authorization
@logger(obj=__name__)
def get_balances():
    """ /v1/wallet/balances """
    header = {'Authorization': Config.API_TOKEN,
              'nonce': str(int(time.time()))}
    req = requests.get('%s/balances/' % (BASE_URL), headers=header)
    return req.json()


@Authorization
@logger(obj=__name__)
def get_withdrawals(withdrawal_id=None):
    """ /v1/wallet/withdrawals/:withdrawal_id """
    header = {'Authorization': Config.API_TOKEN,
              'nonce': str(int(time.time()))}
    if withdrawal_id:
        req = requests.get('%s/withdrawals/%s' % (BASE_URL, withdrawal_id),
                           headers=header)
    else:
        req = requests.get('%s/withdrawals/' % (BASE_URL), headers=header)
    return req.json()


@Authorization
@logger(obj=__name__)
def get_limits_withdrawal():
    """ /v1/wallet/limits/withdrawal """
    header = {'Authorization': Config.API_TOKEN,
              'nonce': str(int(time.time()))}
    req = requests.get('%s/limits/withdrawal/' % (BASE_URL), headers=header)
    return req.json()
