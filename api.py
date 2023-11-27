import json

import requests
from requests.structures import CaseInsensitiveDict


class ApiController (object):
    headers = CaseInsensitiveDict()

    def __init__(self, url, token):
        self.base_url = url
        self.token = token
        self.headers["X-API-KEY"] = self.token

    def message(self, department: int, name: str, group: str, tg_id: int, message: str):
        data = {
            "department_id": department,
            "name": name,
            "group_n": group,
            "tg_id": tg_id,
            "message": message
        }
        data = json.dumps(data).encode('utf-8')
        # data = ('{'
        #         f'"department_id": {department},'
        #         f'"name": "{name}",'
        #         f'"group_id": {group},'
        #         f'"tg_id": {tg_id},'
        #         f'"message": "{message}"'
        #         '}').encode('utf-8')
        # print(data)

        resp = requests.put(f'{self.base_url}/question', data=data, headers=self.headers)
        return {'status': resp.status_code, 'response': resp.json()}

    def departments(self):
        resp = requests.get(f'{self.base_url}/departments')
        return {'status': resp.status_code, 'response': resp.json()}

    # def validate_user(self):
    #     resp = requests.get(f'{self.base_url}/')


if __name__ == '__main__':
    a = ApiController('https://sc-back.cullfy.ru', 'huisosi')

    # r = a.message(1, 'влад', '123', 1234567890, 'some message text here')
    # r = a.departments()
    # r = r['response']['data']
    # for line in r:
    #     # print(line)
    #     print(f'{line["name"]}: \n'
    #           f'1. {line["leader"]}\n'
    #           f'2. {line["deputy"]}\n'
    #           f'3. {line["secretary"]}\n'
    #           f'\n'
    #           f'<a href="https://t.me/{line["contact_tg"]}">{line["contact_tg"]}</a>\n'
    #           f'{line["description"]}\n\n')
    print(a)
