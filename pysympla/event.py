from bs4 import BeautifulSoup

class Event:
    def __init__(self, html, title=''):
        self._soup = BeautifulSoup(html, 'html5lib')
        self._confirmed_participants = 0
        self._pending_participants = 0
        self._title = title

    @property
    def confirmed_participants(self):
        if not self._confirmed_participants:
            id = 'spanTotalParticipants'
            self._confirmed_participants = self._soup.find(id=id).get_text()
        return self._confirmed_participants

    @property
    def pending_participants(self):
        if not self._pending_participants:
            id = 'spanTotalPendingParticipants'
            self._pending_participants = self._soup.find(id=id).get_text()
        return self._pending_participants

    @property
    def title(self):
        if not self._title:
            id = 'event-title'
            self._title = self._soup.find(id=id).get_text()
        return self._title
