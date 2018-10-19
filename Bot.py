import os

from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler

import plusplus


def start(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


def perseet(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text="VEDETÄÄN PERSEET")


def paatyyn(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text="päätyyn")


def plussaks(bot, update, args):

    text = ""

    for arg in args:
        text += "\n"
        text += plusplus.toPlus(arg)

    bot.send_message(chat_id=update.message.chat_id, text=text)


def plussasta(bot, update, args):

    text = ""

    for arg in args:
        text += "\n"
        text += plusplus.fromPlus(arg)

    bot.send_message(chat_id=update.message.chat_id, text=text)


def helper(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text="lol joku help")


token = os.environ["TOKEN"]

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token=token)
dispatcher = updater.dispatcher


handlers = {
    'start': start,
    'help': helper,
    'mitatanaantehdaan': perseet,
    'mitatehdaantanaan': perseet,
    'päätyyn': paatyyn,
    'plussaks': plussaks,
    'plussasta': plussasta
}

for key, value in handlers.items():
    handler = CommandHandler(key, value, pass_args=True)
    dispatcher.add_handler(handler)
    print("Added handler for", key)


print("Starting polling")
updater.start_polling()
