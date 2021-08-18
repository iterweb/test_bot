from django.core.management.base import BaseCommand
from django.conf import settings

import requests
import json
import telebot
from telebot import types

from crypton.models import Profile
from preferences import preferences


bot = telebot.TeleBot(settings.TOKEN)

coins = {
    'BTC': ['btc', 'bitcoin', 'биткоин'],
    'ETH': ['eth', 'ethereum', 'эфириум'],
    'DOGE': ['doge', 'dogecoin', 'догикоин']
}


class Command(BaseCommand):
    help = 'Telegram Bot'

    def handle(self, *args, **options):
        bot.polling(none_stop=True)


def exchange(crypto):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    headers = {
        "X-CMC_PRO_API_KEY": settings.COINMARKETCAP_API_KEY,
        "Accept": "application/json"
    }

    parameters = {
        'symbol': crypto
    }

    session = requests.Session()
    session.headers.update(headers)
    data = session.get(url, params=parameters)

    results = (json.loads(data.text)).get('data')
    return results[f'{crypto}']['quote']['USD']['price']


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, preferences.BotPreferences.welcome, reply_markup=choice_crypto())

    chat_id = message.chat.id

    Profile.objects.get_or_create(
                tg_id=chat_id,
                defaults={
                    'tg_username': message.from_user.username,
                    'tg_firstname': message.from_user.first_name,
                    'tg_lastname': message.from_user.last_name,
                }
    )


@bot.message_handler(content_types=["text"])
def send_anytext(message):
    text = message.text.lower()
    chat_id = message.chat.id
    for key, val in coins.items():
        if text in val:
            bot.send_message(chat_id, exchange(key), reply_markup=choice_crypto())
            break
    else:
        bot.send_message(chat_id, preferences.BotPreferences.error_message, reply_markup=choice_crypto())


def choice_crypto():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btc = types.KeyboardButton(preferences.BotPreferences.btc)
    eth = types.KeyboardButton(preferences.BotPreferences.eth)
    doge = types.KeyboardButton(preferences.BotPreferences.doge)
    markup.add(btc, eth, doge)
    return markup
