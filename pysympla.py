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
        response = requests.get(self.URLS['PARTICIPANTS'], params=params,
                                cookies=self.cookies)
        if response.status_code == 200:
            return Event(response.text)
        else:
            raise Exception('Get event failed. Check event id.')

class Event:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html5lib')
        self._confirmed_participants = 0
        self._pending_participants = 0

    @property
    def confirmed_participants(self):
        if not self._confirmed_participants:
            id = 'spanTotalParticipants'
            self._confirmed_participants = self.soup.find(id=id).get_text()
        return self._confirmed_participants

    @property
    def pending_participants(self):
        if not self._pending_participants:
            id = 'spanTotalPendingParticipants'
            self._pending_participants = self.soup.find(id=id).get_text()
        return self._pending_participants
