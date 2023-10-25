from bot_types import ParsingMode, AvailableLanguages


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

    __strings: dict[ParsingMode, dict[AvailableLanguages, dict[str, str]]] = {
        'HTML': {
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
                                      'link1'
                                      'link2',
                'inform_class': 'проход к аудиториям..',
                'subscribe': 'подписки... да, я заебался катать тексты'
            },
        },
        'Markdown': {
            'en': {
                'hello': '*Hello*, world!',
                'test': 'This is a _test_ message',
            },
            'ru': {
                'hello': '*Привет*, мир!',
                'test': 'Это _тестовое_ сообщение',
            },
        },
        'MarkdownV2': {
            'en': {
                'hello': '*Hello*, world\!',
                'test': 'This is a _test_ message',
            },
            'ru': {
                'hello': '*Привет*, мир\!',
                'test': 'Это _тестовое_ сообщение',
            },
        },
        None: {
            'en': {
                'hello': 'Hello, world!',
                'test': 'This is a test message',
            },
            'ru': {
                'hello': 'Привет, мир!',
                'test': 'Это тестовое сообщение',
            },
        },
    }

    def __init__(self, lang: AvailableLanguages = 'ru', parse_mode: ParsingMode = 'HTML'):
        self.lang = lang
        self.parse_mode = parse_mode
        self.load_strings()

    def load_strings(self):
        for i in self.__strings[self.parse_mode][self.lang]:
            setattr(self, i, self.__strings[self.parse_mode][self.lang][i])

    def __repr__(self):
        return f'<BotStrings lang={self.lang} parse_mode={self.parse_mode}>'


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
}

BackPages = {
    '1': '0',
    '2': '0',
    '2-1': '2',
    '2-1-1': '2-1',
    '2-1-2': '2-1',
    '2-2': '2',
    '3': '0',

}


if __name__ == '__main__':
    strings = BotStrings()
    print(strings.parse_mode)
    print(strings.hello)
    print(strings.test)
    print(strings)
