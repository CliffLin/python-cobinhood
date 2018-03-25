from cobinhood.configuration import Config
from cobinhood.http import system, market, wallet, trading, chart
from cobinhood.ws import feed


class Cobinhood(object):
    def __init__(self, API_TOKEN='', LOG_LEVEL='DEBUG'):
        self.config = Config()
        self.config.API_TOKEN = API_TOKEN
        self.config.LOG_LEVEL = LOG_LEVEL
        self.system = system.System(self.config)
        self.market = market.Market(self.config)
        self.wallet = wallet.Wallet(self.config)
        self.trading = trading.Trading(self.config)
        self.chart = chart.Chart(self.config)
        self.ws = feed.CobinhoodWS(self.config, obj=self)
