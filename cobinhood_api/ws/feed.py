import logging
import traceback
import time
import json
import threading
import websocket
import coloredlogs
from cobinhood_api.ws.response import ExchangeData

logger = logging.getLogger('cobinhood.ws')


class CobinhoodWS(object):
    def __init__(self, config, **parameters):
        coloredlogs.install(level=config.LOG_LEVEL, logger=logger)
        self.pingThread = threading.Thread(target=self.ping)
        self.pingThread.setDaemon(True)
        self._subscribe = []
        self.ws = None
        self.token = config.API_TOKEN
        self.config = config
        self.msg_callback = None
        self.exchange_data = ExchangeData()
        self.parameters = parameters

    def start(self, subscribe=None, on_message=None):
        if on_message:
            self.msg_callback = on_message
        if subscribe:
            self._subscribe = subscribe
        if self.token != '':
            headers = 'Authorization: %s' % self.token
            self.ws = websocket.WebSocketApp(self.config.WS_URL,
                                             on_open=self.on_open,
                                             on_close=self.on_close,
                                             on_error=self.on_error,
                                             on_message=self.on_message,
                                             header=[headers])
        else:
            self.ws = websocket.WebSocketApp(self.config.WS_URL,
                                             on_open=self.on_open,
                                             on_close=self.on_close,
                                             on_message=self.on_message)
        while True:
            try:
                self.ws.run_forever()
            except Exception as e:
                logger.error('WS Ping Error: %s', e)
            time.sleep(10)

    def ping(self):
        while True:
            try:
                self.ws.send('{"action": "ping"}')
            except Exception as e:
                logger.error('WS Ping Error: %s', e)
            time.sleep(30)

    def on_error(self, unused_ws, error):
        logger.error('WS Error: %s', error)

    def on_open(self, unused_ws):
        logger.info('Websocket Connected!')
        for topic in self._subscribe:
            self.post_message(str(topic))
        if not self.pingThread.is_alive():
            self.pingThread.start()

    def on_close(self, unused_ws):
        logger.info('Websocket Closed!')

    def on_message(self, unused_ws, msg):
        try:
            logger.debug(msg)
            msg = json.loads(msg)
            if 'channel_id' in msg.keys():
                if 'event' in msg.keys():
                    event = msg['event']
                elif 'update' in msg.keys():
                    event = 'update'
                elif 'snapshot' in msg.keys():
                    event = 'snapshot'
                else:
                    event = ''
                logger.info('Receive: %s %s', event, msg['channel_id'])
            if 'actoion' not in msg.keys() and 'event' not in msg.keys():
                self.exchange_data.dispatcher(msg)
            if self.msg_callback:
                self.msg_callback(self.parameters['obj'], msg)
        except Exception as e:
            logger.error('%s, %s', msg, e)
            logger.error(traceback.print_exc())

    def post_message(self, msg):
        logger.info('Send %s', msg)
        self.ws.send(msg)
