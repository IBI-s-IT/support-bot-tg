from typing import Literal

ConfigFormat = Literal['env', 'json', 'ini']
ParsingMode = Literal[None, 'HTML', 'Markdown', 'MarkdownV2']
AvailableLanguages = Literal['en', 'ru']
