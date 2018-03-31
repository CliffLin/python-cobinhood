from cobinhood_api.configuration import Config
from cobinhood_api.http import system, market, wallet, trading, chart
from cobinhood_api.ws import feed


class Cobinhood(object):
    def __init__(self, **parameters):
        self.config = Config()
        for key, value in parameters.items():
            exec('self.config.%s = "%s"' % (key, value))
        self.system = system.System(self.config)
        self.market = market.Market(self.config)
        self.wallet = wallet.Wallet(self.config)
        self.trading = trading.Trading(self.config)
        self.chart = chart.Chart(self.config)
        self.ws = feed.CobinhoodWS(self.config, obj=self)
