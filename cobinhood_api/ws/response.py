class ExchangeData(object):
    def __init__(self):
        self.ticker = {}
        self.orderbook = {}
        self.candle = {}
        self.trade = {}
        self.order = None

    def dispatcher(self, msg):
        if '.' in msg['channel_id']:
            channel, target = msg['channel_id'].split('.')[0:2]
        else:
            channel = msg['channel_id']
        if channel == 'ticker':
            if target in self.ticker.keys():
                self.ticker[target].response(msg)
            else:
                new_ticker = Ticker(target)
                new_ticker.response(msg)
                self.ticker[target] = new_ticker
        elif channel == 'order-book':
            precision = msg['channel_id'].split('.')[2]
            if target in self.orderbook.keys():
                if precision in self.orderbook[target].keys():
                    self.orderbook[target][precision].response(msg)
                else:
                    new_orderbook = Orderbook(target, precision)
                    new_orderbook.response(msg)
                    self.orderbook[target][precision] = new_orderbook
            else:
                new_orderbook = Orderbook(target, precision)
                new_orderbook.response(msg)
                self.orderbook.update({target: {precision: new_orderbook}})
        elif channel == 'candle':
            timeframe = msg['channel_id'].split('.')[2]
            if target in self.candle.keys():
                if timeframe in self.candle[target].keys():
                    self.candle[target][timeframe].response(msg)
                else:
                    new_candle = Candle(target, timeframe)
                    new_candle.response(msg)
                    self.candle[target][timeframe] = new_candle
            else:
                new_candle = Candle(target, timeframe)
                new_candle.response(msg)
                self.candle.update({target: {timeframe: new_candle}})
        elif channel == 'trade':
            if target in self.trade.keys():
                self.trade[target].response(msg)
            else:
                new_trade = Trade(target)
                new_trade.response(msg)
                self.trade[target] = new_trade
        elif channel == 'order':
            if self.order:
                self.order.response(msg)
            else:
                new_order = Order()
                new_order.response(msg)
                self.order = new_order


class Ticker(object):
    def __init__(self, name):
        self.object = name
        self.data = None

    def response(self, msg):
        if 'snapshot' in msg:
            msg = msg['snapshot']
        else:
            msg = msg['update']
        self.data = {
            'PRICE': msg[1],
            'HIGHEST_BID': msg[2],
            'LOWEST_ASK': msg[3],
            '24H_VOLUME': msg[4],
            '24H_HIGH': msg[5],
            '24H_LOW': msg[6],
            '24H_OPEN': msg[7],
            'TIME_STAMP': msg[8]}


class Orderbook(object):
    def __init__(self, trading_pair, precision):
        self.trading_pair = trading_pair
        self.precision = precision
        self.data = None

    def response(self, msg):
        if 'snapshot' in msg:
            self.data = msg['snapshot']
        elif 'update' in msg:
            msg = msg['update']
            for bid in msg['bids']:
                self.data['bids'] = list(reversed(
                    self.update(list(reversed(self.data['bids'])), bid)))
            for ask in msg['asks']:
                self.data['asks'] = self.update(self.data['asks'], ask)

    def update(self, orig, update):
        left = 0
        right = len(orig) - 1
        while True:
            if left >= right:
                break
            mid = (left + right) / 2
            if orig[mid][0] == update[0]:
                left = mid
                break
            elif orig[mid][0] > update[0]:
                right = mid - 1
            elif orig[mid][0] < update[0]:
                left = mid + 1
        if orig[left][0] == update[0]:
            orig[left][1] = str(int(orig[left][1]) + int(update[1]))
            if orig[left][1] == '0':
                orig.pop(left)
            else:
                orig[left][2] = str(float(orig[left][2]) + float(update[2]))
        elif orig[left][0] > update[0]:
            orig.insert(left, update)
        elif orig[left][0] < update[0]:
            orig.insert(left+1, update)
        return orig


class Candle(object):
    def __init__(self, trading_pair, timeframe):
        self.trading_pair = trading_pair
        self.timeframe = timeframe
        self.data = None

    def response(self, msg):
        if 'snapshot' in msg:
            self.data = msg['snapshot']
        elif 'update' in msg:
            msg = msg['update']
            if self.data[len(self.data)-1][0] == msg[0]:
                self.data[len(self.data)-1] = msg
            else:
                self.data.append(msg)


class Trade(object):
    def __init__(self, trading_pair):
        self.trading_pair = trading_pair
        self.data = None

    def response(self, msg):
        if 'snapshot' in msg:
            self.data = msg['snapshot']
        elif 'update' in msg:
            msg = msg['update']
            for m in msg:
                self.data.insert(0, m)


class Order(object):
    def __init__(self):
        self.data = None

    def response(self, msg):
        self.data = msg['update']
