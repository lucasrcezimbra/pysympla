import pytest

from pysympla.sympla import Event


@pytest.fixture
def event(html_event):
    return Event(html_event)


def test_confirmed_participants(event):
    assert type(event.confirmed_participants) == int
    assert event.confirmed_participants == 2


def test_pending_participants(event):
    assert type(event.pending_participants) == int
    assert event.pending_participants == 0


def test_title(event):
    assert event.title == 'Event Test'
