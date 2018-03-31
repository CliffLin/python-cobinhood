class Config(object):
    API_VERSION = 'v1'
    API_TOKEN = ''
    BASE_URL = 'https://api.cobinhood.com/%s' % API_VERSION
    LOG_LEVEL = 'DEBUG'
    WS_URL = 'wss://ws.cobinhood.com/ws'
    DEV = False
