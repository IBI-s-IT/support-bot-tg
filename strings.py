from bot_types import ParsingMode, AvailableLanguages


class BotStrings:
    hello: str
    test: str

    __strings: dict[ParsingMode, dict[AvailableLanguages, dict[str, str]]] = {
        'HTML': {
            'en': {
                'hello': '<b>Hello</b>, world!',
                'test': 'This is a <i>test</i> message',
            },
            'ru': {
                'hello': '<b>Привет</b>, мир!',
                'test': 'Это <i>тестовое</i> сообщение',
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


if __name__ == '__main__':
    strings = BotStrings()
    print(strings.parse_mode)
    print(strings.hello)
    print(strings.test)
    print(strings)
