import os
import random

from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler

import plusplus


baarit = [
    'Mennään Xanax baariin',
    'Lähetään SEON baariin',
    'vedetään viinaa',
    'VEDETÄÄN PERSEET',
    'vois mennä finishaa c++ projekti',
    'vetemään perseet pirjo 50v juhlissa',
    'VETÄMÄÄN PERSEET',
    'Vätköille',
    'pakko mennä aamutakkisillikselle',
]


def start(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text="kiitos ryhmään pääsystä. nyt vedetään perseet.")


def perseet(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text="VEDETÄÄN PERSEET")


def rare(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text="Nyt vedetään jussia")


def kolikko(bot, update, args):
    if random.randint(1, 2) == 1:
        bot.send_message(chat_id=update.message.chat_id, text="Heitettin KRUUNA. Eli VEDETÄÄNKÖ PERSEET")
    else:

        lause = random.choice(baarit)
        s = "Heitettiin KLAAVA. Eli " + lause

        if random.randint(0, 8) == 2:
           s = plusplus.toPlus(s)

        bot.send_message(chat_id=update.message.chat_id, text=s)


def tanaan(bot, update, args):
    if random.randint(-69, 69) == 2:
        rare(bot, update, args)
    else:
        r = random.randint(0, 8)

        if r <= 4:
            perseet(bot, update, args)
        if r == 5:
            paatyyn(bot, update, args)
        if r == 6:
            paatyynyyn(bot, update, args)
        if r == 8 or r == 7:
            saukko(bot, update, args)


def saukko(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text="/saukko@saukkobot")


def paatyyn(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text="päätyyn")


def paatyynyyn(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text="ai pää tyynyyn vai? lol, hyvä vitsi. vois vetää PERSEET")


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
    'plussaks': plussaks,
    'plussaksi': plussaks,
    'plussast': plussasta,
    'plussasta': plussasta,
    'tanaan': tanaan,
    'kolikko': kolikko,
    'heitakolikkoa': kolikko

}

for key, value in handlers.items():
    handler = CommandHandler(key, value, pass_args=True)
    dispatcher.add_handler(handler)
    print("Added handler for", key)

print("Starting polling")
updater.start_polling()
