from telebot import TeleBot
from telebot.types import Message, CallbackQuery
from config import Config
from excatcher import error_handler
from static import BotStrings, BackPages
from static import MarkupPages as pages

import commands


config = Config('.env', config_format='env')
bot = TeleBot(config.API_TOKEN, parse_mode=config.PARSE_MODE)

strings = BotStrings(parse_mode=bot.parse_mode)
c = commands.BotCommands(bot, strings)

page: str  # needs to be updated for storing more information


@bot.message_handler(commands=['start'])
def start(message: Message):
    global page
    page = '0'
    c.reply(message, page)


@bot.message_handler(commands=['appeal'])
def appeal(message: Message):
    global page
    page = '1'
    c.reply(message, page)


@bot.message_handler(commands=['inform'])
def appeal(message: Message):
    global page
    page = '2'
    c.reply(message, page)


@bot.message_handler(commands=['subscribe'])
def appeal(message: Message):
    global page
    page = '3'
    c.reply(message, page)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call: CallbackQuery):
    global page
    if call.data == 'go_back':
        page = BackPages[page]
        c.reply(call, page)
    else:
        page = list(pages.keys())[list(pages.values()).index(call.data)]
        c.reply(call, page)


@error_handler(exits=False)
def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()
