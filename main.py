from telebot import TeleBot, apihelper
from telebot.types import Message, CallbackQuery

from api import ApiController
from config import Config
from excatcher import error_handler
from static import BotStrings, BackPages
from static import MarkupPages

import commands


config = Config('.env', config_format='env')
bot = TeleBot(config.API_TOKEN, parse_mode='HTML')

if config.TEST_SERVER == '1':
    apihelper.API_URL = 'https://api.telegram.org/bot{0}/test/{1}'

api = ApiController(config.SC_API_URL, config.SC_API_TOKEN)

strings = BotStrings(api)
c = commands.BotCommands(bot, strings, api)

page: str


@bot.message_handler(commands=['start'])
def start(message: Message):
    global page
    page = '0'
    c.reply(message, page)


@bot.message_handler(commands=['appeal'])
def ask(message: Message):

    c.get_question(message)


# @bot.message_handler(commands=['inform'])
# def inform(message: Message):
#     global page
#     page = '2'
#     c.reply(message, page)
#
#
# @bot.message_handler(commands=['subscribe'])
# def subscribe(message: Message):
#     global page
#     page = '3'
#     c.reply(message, page)


@bot.message_handler(commands=['admin'])
def panel(message: Message):
    c.panel(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call: CallbackQuery):
    global page
    if call.data == 'go_back':
        try:
            page = BackPages[page]
        except KeyError:
            page = '0'
        except NameError:
            page = '0'
    else:
        try:
            page = list(MarkupPages.keys())[list(MarkupPages.values()).index(call.data)]
        except KeyError:
            page = '0'
    c.reply(call, page)


@error_handler(exits=False)
def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()
