import os

from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler

import plusplus


def start(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text="kiitos ryhmään pääsystä. nyt vedetään perseet.")


def perseet(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text="VEDETÄÄN PERSEET")


def itisknown(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text="it is known")


def paatyyn(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text="päätyyn")


def plussaks(bot, update, args):
    if len(args) != 0:
        text = plusplus.toPlus(" ".join(args))
    else:
        text = "Ei plussia annettu????? wtf"

    bot.send_message(chat_id=update.message.chat_id, text=text)


def plussasta(bot, update, args):
    if len(args) != 0:
        text = " ".join(args)
        try:
            text = plusplus.fromPlus(text)
        except Exception as e:
            text = "opettele kirjottaa vitun pelle"
    else:
        text = "/saukko@saukkobot"

    bot.send_message(chat_id=update.message.chat_id, text=text)


def helper(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text="lol joku help")


token = os.getenv("TOKEN")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token=token)
dispatcher = updater.dispatcher


handlers = {
    'start': start,
    'help': helper,
    'mitatanaantehdaan': perseet,
    'mitatehdaantanaan': perseet,
    'mitatehaan': perseet,
    'perseet': itisknown,
    'päätyyn': paatyyn,
    'paatyyn': paatyyn,
    'plussaks': plussaks,
    'plussaksi': plussaks,
    'plussast': plussasta,
    'plussasta': plussasta,
    'pää tyynyyn': paatyyn,
    'paatyynyyn': paatyyn

}

for key, value in handlers.items():
    handler = CommandHandler(key, value, pass_args=True)
    dispatcher.add_handler(handler)
    print("Added handler for", key)


print("Starting polling")
updater.start_polling()
