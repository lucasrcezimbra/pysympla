import pytest

from pysympla.sympla import Event 


@pytest.fixture
def html_event():
    return '''
<div id="event-main-text">
    <div id="event-title"><span><a href="/sobre-o-evento?id=1">Event Test</a></span></div>
    <div id="event-date-time">
        Quinta, 27 de Agosto de 2020, 12h
    </div>
</div>
<div id="stats-div" style="float: left; width: 100%; margin-bottom: 4px;">
    <div class="stats-counter" style="float: left; padding: 0 25px 0 0;">
        <span class="label">Confirmados:</span>
        <span id="spanTotalParticipants" class="value">2</span>
    </div>
    <div class="stats-counter"  style="float: left; padding: 0 25px 0 0;">
        <span class="label">Pagamento pendente:</span>
        <span id="spanTotalPendingParticipants" class="value">0</span>
    </div>
'''

@pytest.fixture
def event(html_event):
    return Event(html_event)


def test_confirmed_participants(event):
    assert event.confirmed_participants == 2


def test_pending_participants(event):
    assert event.pending_participants == 0


def test_title(event):
    assert event.title == 'Event Test'
