import pytest
from unittest import mock

import requests

from pysympla import Sympla


@pytest.fixture
def response_200():
    response = requests.Response()
    response.status_code = 200
    return response


@pytest.fixture
def authenticated_sympla(monkeypatch, response_200):
    monkeypatch.setattr('requests.post', mock.MagicMock(return_value=response_200))
    return Sympla('email@email.com', '123456')


@pytest.fixture
def http_status_without_200():
    return [
        100, 101, 102,
        201, 202, 203, 204, 205, 206, 207, 208, 226,
        300, 301, 302, 303, 304, 305, 306, 307, 308,
        400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414,
        415, 416, 417, 418, 421, 422, 423, 424, 426, 428, 429, 431, 440, 451,
        500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511
    ]


@pytest.mark.parametrize("http_status", http_status_without_200())
def test_authentication_failure_raise_exception(monkeypatch, http_status):
    ''' Raises Exception if http_status is not 200'''
    response = requests.Response()
    response.status_code = http_status

    monkeypatch.setattr('requests.post', mock.MagicMock(return_value=response))
    with pytest.raises(Exception,
                       match='Authentication failed. Check your credentials.'):
        Sympla('email@email.com', '123456')


def test_authenticate_set_cookies(monkeypatch, response_200):
    response_200.cookies = {'sympla': 'abc123def456'}

    monkeypatch.setattr('requests.post', mock.MagicMock(return_value=response_200))
    sympla = Sympla('email@email.com', '123456')
    assert sympla._cookies == response_200.cookies


def test_authenticate_send_data_and_headers(monkeypatch, response_200):
    username = 'email@email.com'
    password = '12345'
    expected_url = 'https://www.sympla.com.br/access/login'
    expected_headers = {'X-Requested-With': 'XMLHttpRequest'}
    expected_data = {
        'username': username,
        'password': password,
        'rememberMe': True,
    }

    requests_post_mock = mock.MagicMock(return_value=response_200)

    monkeypatch.setattr('requests.post', requests_post_mock)

    Sympla(username, password)
    requests_post_mock.assert_called_with(expected_url,
                                          data=expected_data,
                                          headers=expected_headers)


@pytest.mark.parametrize("http_status", http_status_without_200())
def test_get_event_failure_raise_exception(monkeypatch, http_status,
                                           response_200, authenticated_sympla):
    ''' Raises Exception if http_status is not 200'''
    response = requests.Response()
    response.status_code = http_status

    monkeypatch.setattr('requests.get', mock.MagicMock(return_value=response))

    with pytest.raises(Exception, match='Get event failed. Check event id.'):
        authenticated_sympla.get_event(0)


def test_get_event(monkeypatch, response_200, html_event, authenticated_sympla):
    response = mock.MagicMock(text=html_event, status_code=200)

    monkeypatch.setattr('requests.get', mock.MagicMock(return_value=response))

    event = authenticated_sympla.get_event(1)

    assert event.title == 'Event Test'
    assert event.confirmed_participants == 2
    assert event.pending_participants == 0


def test_get_events(monkeypatch, response_200, html_events, authenticated_sympla):
    response = mock.MagicMock(text=html_events, status_code=200)

    monkeypatch.setattr('requests.get', mock.MagicMock(return_value=response))

    event = list(authenticated_sympla.get_events())[0]

    assert event.title == 'Teste'
