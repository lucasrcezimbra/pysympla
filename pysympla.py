import requests
from bs4 import BeautifulSoup

class Sympla:
    BASE_URL = 'https://www.sympla.com.br'
    URLS = {
        'LOGIN': BASE_URL + '/access/login',
        'PARTICIPANTS': BASE_URL + '/participantes-evento',
    }

    def __init__(self, username, password):
        self._authenticate(username, password)

    def _authenticate(self, username, password):
        data = {
            'username': username,
            'password': password,
            'rememberMe': True,
        }
        headers = {'X-Requested-With': 'XMLHttpRequest',}
        response = requests.post(self.URLS['LOGIN'], data=data, headers=headers)
        if response.status_code == 200:
            self.cookies = response.cookies
        else:
            raise Exception('Authentication failed. Check your credentials.')

    def get_event(self, id):
        params = {'id': id}
        response = requests.get(PARTICIPANTS_URL, params=params,
                                cookies=self.cookies)
        if response.status_code == 200:
            return Event(response.text)
        else:
            raise Exception('Get event failed. Check event id.')

class Event:
    def __init__(self, html):
        self.html = html
        self.soup = BeautifulSoup(self.html, 'html5lib')

    def get_confirmed_participants(self):
        return soup.find(id='spanTotalParticipants').get_text()

    def get_pending_participants(self):
        return soup.find(id='spanTotalPendingParticipants').get_text()
