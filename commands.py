from telebot.types import Message, CallbackQuery
from telebot import TeleBot

from api import ApiController
from markups import MessageMarkups
from static import BotStrings, MarkupPages


class BotCommands:
    def __init__(self, bot: TeleBot, strings: BotStrings, api: ApiController):
        self.bot = bot
        self.strings = strings
        self.api = api

    def reply(self, data: CallbackQuery | Message, page):
        page_name = MarkupPages[page]
        if page_name == 'appeal':
            return self.get_question(data)
        markup = getattr(MessageMarkups, page_name)
        text = getattr(self.strings, page_name)

        if isinstance(data, CallbackQuery):
            self.bot.edit_message_text(
                text,
                data.message.chat.id,
                data.message.message_id,
                reply_markup=markup,
                disable_web_page_preview=True
            )
        elif isinstance(data, Message):
            self.bot.send_message(
                data.chat.id,
                text,
                reply_markup=markup,
                disable_web_page_preview=True
            )
        else:
            print('Этой надписи не должно быть, смотри типизацию')

    def get_question(self,  data: CallbackQuery | Message):
        message = data.message if isinstance(data, CallbackQuery) else data
        self.bot.send_message(message.chat.id, self.strings.get_question_name)
        question = []

        def get_q_text(msg: Message):
            question.append(msg.text)
            name, group, text = question
            r = self.api.message(1, name, group, msg.from_user.id, text)
            if r['status'] == 201:
                self.bot.send_message(msg.chat.id, self.strings.question_submit_success)
            else:
                self.bot.send_message(msg.chat.id, self.strings.question_submit_bad)

        def get_q_group(msg: Message):
            question.append(msg.text)
            self.bot.send_message(msg.chat.id, self.strings.get_question_text)
            self.bot.register_next_step_handler(msg, get_q_text)

        def get_q_name(msg: Message):
            question.append(msg.text)
            self.bot.send_message(msg.chat.id, self.strings.get_question_group)
            self.bot.register_next_step_handler(msg, get_q_group)

        self.bot.register_next_step_handler(message, get_q_name)

    def panel(self, message: Message):
        self.bot.send_message(
            message.from_user.id,
            self.strings.panel,
            reply_markup=MessageMarkups.admin,
            disable_web_page_preview=True
        )
