import re

import requests
from bs4 import BeautifulSoup

from pysympla.event import Event


class Sympla:
    BASE_URL = 'https://www.sympla.com.br'
    URLS = {
        'LOGIN': BASE_URL + '/access/login',
        'PARTICIPANTS': BASE_URL + '/participantes-evento',
        'EVENTS': BASE_URL + '/meus-eventos',
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
            self._cookies = response._cookies
        else:
            raise Exception('Authentication failed. Check your credentials.')

    def get_event(self, id):
        try:
            return Event(self._get_event_html(id))
        except:
            raise Exception('Get event failed. Check event id.')

    def _get_event_html(self, id):
        params = { 'id': id }
        response = requests.get(self.URLS['PARTICIPANTS'], params=params,
                                cookies=self._cookies)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception('Get event failed. Check event id.')

    def get_events(self):
        response = requests.get(self.URLS['EVENTS'], cookies=self._cookies)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html5lib')
            html_id = 'event-grid'
            regex_href = re.compile('/sobre-o-evento')
            events = soup.find(id=html_id).find_all('a', href=regex_href)
            for event in events:
                title = event.get_text()
                id = self._get_id_from_a(event)
                html = self._get_event_html(id)

                yield Event(html, title)
        else:
            raise Exception('Get events failed.')

    def _get_id_from_a(self, a):
        href = a.get_attribute_list('href')[0]
        _, id = href.split('=')
        return id
