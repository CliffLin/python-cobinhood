from cobinhood.configuration import Config
from cobinhood.http import system, market, wallet, trading, chart
from cobinhood.ws import feed


class Cobinhood(object):
    def __init__(self, API_TOKEN='', LOG_LEVEL='DEBUG'):
        self.config = Config()
        self.config.API_TOKEN = API_TOKEN
        self.config.LOG_LEVEL = LOG_LEVEL
        self.system = system.System()
        self.market = market.Market()
        self.wallet = wallet.Wallet(token=API_TOKEN)
        self.trading = trading.Trading(token=API_TOKEN)
        self.chart = chart.Chart()
        self.ws = feed.CobinhoodWS(token=API_TOKEN, obj=self)
