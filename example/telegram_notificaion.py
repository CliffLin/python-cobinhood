"""
Cobinhood Order Notificaion on Telegram.
"""
import json
import telegram
from cobinhood_api import Cobinhood
from cobinhood_api.ws.subscribe import Order

TELGRAM_TOKEN = 'YOUR_TELEGRAM_TOKEN'
USER_ID = 'YOUR_TELEGRAM_USER_ID'
BOT = telegram.Bot(token=TELGRAM_TOKEN)

def on_message(cob_obj, msg):
    """
    parameters:
      - cob_obj: Object(Cobinhood)
      - msg: Dict()
    """
    if 'channel_id' in msg.keys() and 'order' == msg['channel_id']:
        if 'update' in msg.keys():
            msg = msg['update']
            text = '%s\n%s\n%s Amount: %s Price: %s' % (
                msg[2].upper(), msg[1], msg[3], msg[7], msg[5])
            BOT.send_message(USER_ID, text=text)

def main():
    cobin_bot = Cobinhood(API_TOKEN='YOUR_API_TOKEN', LOG_LEVEL='DEBUG')
    order = Order()
    cobin_bot.ws.start(subscribe=[order], on_message=on_message)

if __name__ == '__main__':
    main()
