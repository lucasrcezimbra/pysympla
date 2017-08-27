import requests
from bs4 import BeautifulSoup
from decouple import config

BASE_URL = 'https://www.sympla.com.br'
LOGIN_URL = BASE_URL + '/access/login'
PARTICIPANTS_URL = BASE_URL + '/participantes-evento'
SYMPLA_USERNAME = config('SYMPLA_USERNAME')
SYMPLA_PASSWORD = config('SYMPLA_PASSWORD')

data = {
    'username': SYMPLA_USERNAME,
    'password': SYMPLA_PASSWORD,
    'rememberMe': True,
}
HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
}

logged = requests.post(LOGIN_URL, data=data, headers=HEADERS)

CHIMARUNPOA_ID = 168054
chimapoa = requests.get(PARTICIPANTS_URL, params={'id': CHIMARUNPOA_ID}, cookies=logged.cookies)

soup = BeautifulSoup(chimapoa.text, 'html5lib')
confirmed_participants = soup.find(id='spanTotalParticipants').get_text()
pending_participants = soup.find(id='spanTotalPendingParticipants').get_text()
confirmed_participants, pending_participants
