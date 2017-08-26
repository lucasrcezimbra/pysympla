
# coding: utf-8

# In[1]:


import requests
from decouple import config
from bs4 import BeautifulSoup


# In[27]:


BASE_URL = 'https://www.sympla.com.br'
LOGIN_URL = BASE_URL + '/access/login'
PARTICIPANTS_URL = BASE_URL + '/participantes-evento'
SYMPLA_USERNAME = config('SYMPLA_USERNAME')
SYMPLA_PASSWORD = config('SYMPLA_PASSWORD')


# In[17]:


data = {
    'username': SYMPLA_USERNAME,
    'password': SYMPLA_PASSWORD,
    'rememberMe': True,
}
headers = {
    'X-Requested-With': 'XMLHttpRequest',
}


# In[32]:


logged = requests.post(LOGIN_URL, data=data, headers=headers)
logged


# In[33]:


CHIMARUNPOA_ID = 168054
chimapoa = requests.get(PARTICIPANTS_URL, params={'id': CHIMARUNPOA_ID}, cookies=logged.cookies, headers=headers)
chimapoa


# In[34]:


soup = BeautifulSoup(chimapoa.text, 'html5lib')
confirmed_participants = soup.find(id='spanTotalParticipants').get_text()
pending_participants = soup.find(id='spanTotalPendingParticipants').get_text()
confirmed_participants, pending_participants


# In[ ]:




