from telebot.types import Message, CallbackQuery
from telebot import TeleBot
from markups import MessageMarkups
from static import BotStrings, MarkupPages


class BotCommands:
    def __init__(self, bot: TeleBot, strings: BotStrings):
        self.bot = bot
        self.strings = strings

    def reply(self, data: CallbackQuery | Message, page):
        page_name = MarkupPages[page]
        markup = getattr(MessageMarkups, page_name)
        text = getattr(self.strings, page_name)

        if isinstance(data, CallbackQuery):
            self.bot.edit_message_text(
                text,
                data.message.chat.id,
                data.message.message_id,
                reply_markup=markup
            )
        elif isinstance(data, Message):
            self.bot.send_message(
                data.chat.id,
                text,
                reply_markup=markup
            )
        else:
            print('Этой надписи не должно быть, смотри типизацию')
