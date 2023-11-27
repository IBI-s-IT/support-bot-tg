from api import ApiController
from bot_types import AvailableLanguages


class Departments:
    deps: dict | None

    def __init__(self, api: ApiController):
        deps = api.departments()
        self.deps = deps['response']['data'] if deps['status'] == 200 else None

    def __repr__(self):
        d_list = ''
        if self.deps is None:
            return '\n<i>ошибка при загрузке информации</i>\n'
        for line in self.deps:
            if 'Председатель' in line['name']:
                d_list += f'<b>{line["name"]}:</b>\n'
                d_list += f'<b><i>{line["leader"]}</i></b>\n\n'
                d_list += f'<i>{line["description"]}</i>\n\n'
            else:
                d_list += f'<b>{line["name"]}: </b>\n'
                d_list += f'<i>{line["description"]}</i>\n'
                d_list += '\n'
                d_list += f'Глава: {line["leader"]}\n'
            d_list += f'Заместитель: {line["deputy"]}\n' if line['deputy'] != '-' else ''
            d_list += f'Секретарь: {line["secretary"]}\n' if line['secretary'] != '-' else ''
            d_list += '\n'
            d_list += f'Контактное лицо: @{line["contact_tg"]}\n\n'
        return d_list


class BotStrings:
    hello: str
    test: str
    main: str
    appeal: str
    inform: str
    inform_resources: str
    resources_channels: str
    resources_ibi_s_it: str
    inform_class: str
    subscribe: str
    ss_info: str
    get_question_name: str
    get_question_group: str
    get_question_text: str
    question_submit_success: str
    question_submit_bad: str

    __strings: dict[AvailableLanguages, dict[str, str]] = {
        'en': {
            'hello': '<b>Hello</b>, world!',
            'test': 'This is a <i>test</i> message',
        },
        'ru': {
            'hello': '<b>Привет</b>, мир!',
            'test': 'Это <i>тестовое</i> сообщение',
            'main': '🎓 <b>Дорогие студенты!</b> 🎓 \n'
                    'Вас приветствует бот студенческого совета МБИ! Наша цель - создать великолепное '
                    'образовательное сообщество, где каждый из вас может расцвести и достичь своих целей. '
                    'Мы здесь, чтобы поддерживать вас и слушать ваши вопросы, идеи и заботы.\n'
                    '\n'
                    '🤝 <b><i>Как мы можем помочь вам:</i></b>'
                    '\n'
                    '1. <i>Ответим на ваши вопросы по учебе.</i>\n'
                    '2. <i>Поможем разрешить возникшие проблемы и сложности.</i>\n'
                    '3. <i>Информируем о мероприятиях и возможностях в университете.</i>\n'
                    '\n'
                    'Не стесняйтесь обращаться к нам! Мы здесь, чтобы сделать ваше студенческое путешествие '
                    'незабвенным и успешным. Пусть этот университетский год будет наполнен '
                    'яркими впечатлениями и новыми возможностями! \n'
                    '\n'
                    'С любовью и поддержкой,\n'
                    'Бот Студенческого Совета МБИ 📘✨',
            'ss_info': 'Студенческий совет МБИ \n'
                       '\n'
                       'Ключевые лица студенческого совета: \n'
                       '—————————————————————\n'
                       '<i>placeholder</i>'
                       'Но спешим заметить, что основное взаимодействие должно происходить через бота, а писать им '
                       'можно только в случае срочности и крайней необходимости.',
            'appeal': '<b>Вопрос студсовету</b>\n'
                      '\n'
                      'Если у вас возник вопрос, вы можете задать его в любой момент.\n'
                      'Мы здесь чтоб вам помочь!',
            'inform': '<b>База знаний</b>\n'
                      '\n'
                      'В этом разделе вы найдете ответы на часто задаваемые вопросы и прочую информацию, '
                      'которая может быть полезна для каждого студента МБИ',
            'inform_resources': '<b>Ссылки на полезные ресурсы</b>\n'
                                '\n'
                                '<i><b>В этом разделе находятся:</b>\n'
                                'Сайт МБИ\n'
                                'Каналы в соц. сетях\n'
                                'Приложения и боты для студентов\n'
                                'Прочие ссылки..</i>',
            'resources_channels': '<b>Ссылки на ресурсы от института:</b>\n'
                                  '\n'
                                  'sth',
            'resources_ibi_s_it': '<b>Ссылки на ресурсы от студсовета:</b>\n'
                                  '\n'
                                  '<a href="https://apps.apple.com/ru/app/ibi-lounge/id6459472308">IBI Lounge IOS</a>\n'
                                  '<a href="https://t.me/ibi_rasp_bot">Бот Расписание</a>\n'
                                  '<a href="https://t.me/ibi_decanat_bot">Бот Абитуриенту</a>\n'
                                  '<a href="https://t.me/ibi_sc_bot">Бот Студсовета</a>',
            'inform_class': 'проход к аудиториям..',
            'subscribe': 'подписки... да, я заебался катать тексты',
            'get_question_name': 'Как вас зовут?',
            'get_question_group': 'Из какой вы группы?',
            'get_question_text': 'Напишите ваш вопрос:',
            'question_submit_success': 'Ваше обращение принято и в ближайшее время будет обработано.',
            'question_submit_bad': 'Произошла неизвестная ошибка при обработке обращения, попробуйте позже.'
        },
    }

    def __init__(self, api: ApiController, lang: AvailableLanguages = 'ru'):
        self.api = api
        self.lang = lang
        self.load_strings()

    def load_strings(self):
        for i in self.__strings[self.lang]:
            setattr(self, i, self.__strings[self.lang][i])
        deps = Departments(self.api)
        self.ss_info = self.ss_info.replace('<i>placeholder</i>', str(deps))

    def __repr__(self):
        return f'<BotStrings lang={self.lang}>'


ClassList = {
    'МС': [
        '10', '12',
        '22', '24',
        '31', '32', '33', '34',
        '42', '43', '44', '45',
        '51', '52', '53', '54', '58'
    ],
    'Н': [
        '425', '430'
    ]
}

MarkupPages = {
    '0': 'main',
    '1': 'appeal',
    '2': 'inform',
    '2-1': 'inform_resources',
    '2-1-1': 'resources_channels',
    '2-1-2': 'resources_ibi_s_it',
    '2-2': 'inform_class',
    '3': 'subscribe',
    '4': 'ss_info'
}

BackPages = {
    '1': '0',
    '2': '0',
    '2-1': '2',
    '2-1-1': '2-1',
    '2-1-2': '2-1',
    '2-2': '2',
    '3': '0',
    '4': '0'

}


if __name__ == '__main__':
    strings = BotStrings()
    print(strings.hello)
    print(strings.test)
    print(strings)
