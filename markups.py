from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


class MessageMarkups:
    test: InlineKeyboardMarkup = InlineKeyboardMarkup()
    test.add(InlineKeyboardButton('Test', callback_data='test'))
