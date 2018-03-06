import json


class Subscribe(object):
    action = 'subscribe'


class Trade(Subscribe):
    def __init__(self, trading_pair_id):
        self.type = 'trade'
        self.action = super(Trade, self).action
        self.trading_pair_id = trading_pair_id

    def __str__(self):
        return json.dumps({
            'type': self.type,
            'action': self.action,
            'trading_pair_id': self.trading_pair_id})


class Orderbook(Subscribe):
    def __init__(self, trading_pair_id, precision=None):
        self.type = 'order-book'
        self.action = super(Orderbook, self).action
        self.trading_pair_id = trading_pair_id
        self.precision = precision

    def __str__(self):
        return json.dumps({
            'type': self.type,
            'action': self.action,
            'trading_pair_id': self.trading_pair_id,
            'precision': self.precision})


class Ticker(Subscribe):
    def __init__(self, trading_pair_id):
        self.type = 'ticker'
        self.action = super(Ticker, self).action
        self.trading_pair_id = trading_pair_id

    def __str__(self):
        return json.dumps({
            'type': self.type,
            'action': self.action,
            'trading_pair_id': self.trading_pair_id})


class Candle(Subscribe):
    def __init__(self, trading_pair_id, timeframe):
        self.type = 'candle'
        self.action = super(Candle, self).action
        self.trading_pair_id = trading_pair_id
        self.timeframe = timeframe

    def __str__(self):
        return json.dumps({
            'type': self.type,
            'action': self.action,
            'trading_pair_id': self.trading_pair_id,
            'timeframe': self.timeframe})


class Order(Subscribe):
    def __init__(self):
        self.type = 'order'
        self.action = super(Order, self).action

    def __str__(self):
        return json.dumps({
            'type': self.type,
            'action': self.action})
