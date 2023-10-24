import os
from dotenv import dotenv_values
from excatcher import error_handler
from bot_types import ConfigFormat


class Config (object):
    @error_handler(exits=True)
    def __init__(self, path, config_format: ConfigFormat = 'env'):

        self.PARSE_MODE = None
        config: dict[str, str | None] = {}

        if config_format == 'env':

            # check if .env file exists
            if not os.path.isfile(path):
                raise FileNotFoundError('File .env not found')

            config = dotenv_values(path)
        elif config_format == 'json':
            raise NotImplementedError('JSON config format is not implemented yet')
        elif config_format == 'ini':
            raise NotImplementedError('INI config format is not implemented yet')

        # check if all required variables are set
        required: list[str] = ['API_TOKEN']
        for key in required:
            if key not in config:
                raise KeyError(f'Required variable "{key}" not set in {path}')

        self.API_TOKEN = config['API_TOKEN']
        self.PARSE_MODE = config['PARSE_MODE'] if 'PARSE_MODE' in config and config['PARSE_MODE'] != '' else None

    def __repr__(self):
        return f'<Config API_TOKEN={self.API_TOKEN}>'


@error_handler(exits=True)
def main():
    c = Config('.env', config_format='env')
    print(c.API_TOKEN)
    print(c.PARSE_MODE)


if __name__ == '__main__':
    main()
