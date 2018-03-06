"""
Cobinhood Order Notificaion on Telegram.
"""
import json
import telegram
from cobinhood.ws.feed import CobinhoodWS
from cobinhood.ws.subscribe import Order
from cobinhood.configuration import Config

Config.API_TOKEN = 'YOUR_COBINHOOD_API_TOKEN'
TELGRAM_TOKEN = 'YOUR_TELEGRAM_TOKEN'
USER_ID = 'YOUR_TELEGRAM_USER_ID'
BOT = telegram.Bot(token=TELGRAM_TOKEN)

def on_message(msg):
    if 'channel_id' in msg.keys() and 'order' == msg['channel_id']:
        if 'update' in msg.keys():
            msg = msg['update']
            text = '%s\n%s\n%s Amount: %s Price: %s' % (
                msg[2].upper(), msg[1], msg[3], msg[7], msg[5])
            BOT.send_message(USER_ID, text=text)

def main():
    c = CobinhoodWS()
    ticker = Order()
    c.start(subscribe=[ticker], on_message=on_message)

if __name__ == '__main__':
    main()
