import json
import logging
import coloredlogs
import time
import sys
from threading import Thread
from uuid import uuid4
from cobinhood_api import Cobinhood
from cobinhood_api.ws import feed
from cobinhood_api.ws.subscribe import Trade
from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.utils.helpers import escape_markdown

TELGRAM_TOKEN = ''
TRADING_PAIR_LIST = ['COB-ETH', 'COB-BTC', 'COB-USDT']

logger = logging.getLogger('telegram_bot')
coloredlogs.install(level='INFO', logger=logger)

cex = Cobinhood(LOG_LEVEL='INFO')
all_trading_pair = []
all_trading_pair_ts = time.time()

def GetTradingPair():
    global all_trading_pair
    all_trading_pair = [] 
    res = cex.market.get_trading_pairs()
    for td_pair in res['result']['trading_pairs']:
        all_trading_pair.append(td_pair['id'])
    all_trading_pair_ts = time.time()


def price(bot, update):
    stats = cex.market.get_stats()
    ret_text = ''
    for trading_pair in TRADING_PAIR_LIST:
        ret_text += '%s: %s %s\n' % (
            trading_pair,
            stats['result'][trading_pair]['last_price'],
            trading_pair.split('-')[1])
    update.message.reply_text(ret_text)

def inlinequery(bot, update):
    if not all_trading_pair or time.time() - all_trading_pair_ts > 60*60*24:
        cex.ws.ws.keep_running = False
        cex.ws.ws.close()
        WebsocketConnect()

    query = update.inline_query.query
    results = []
    for td_pair in cex.ws.exchange_data.trade.keys():
        if td_pair.startswith(query):
            results.append(
                InlineQueryResultArticle(
                    id=uuid4(),
                    title=td_pair,
                    input_message_content=InputTextMessageContent(
                    '%s: %s' % (
                        td_pair,
                        cex.ws.exchange_data.trade[td_pair].data[-1][2]))))

    update.inline_query.answer(results)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)

def WebsocketConnect():
    GetTradingPair()
    subscribe_list = []
    for td_pair in all_trading_pair:
        subscribe_list.append(Trade(td_pair))
    proc = Thread(target=cex.ws.start, kwargs={'subscribe': subscribe_list})
    proc.start()

def main():
    
    WebsocketConnect()
    
    updater = Updater(token=TELGRAM_TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('price', price))
    dp.add_handler(InlineQueryHandler(inlinequery))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

