import pytest
from unittest import mock

import requests

from pysympla import Sympla


@pytest.fixture
def html_events():
    return '''
# NOQA
<div class="grid-view rounded" id="event-grid">
  <table class="items">
    <thead>
      <tr>
        <th id="event-grid_c0">Status</th>
        <th id="event-grid_c1"><a class="sort-link" href="/meus-eventos?Event_sort=NAME">Nome</a></th>
        <th id="event-grid_c2"><a class="sort-link" href="/meus-eventos?Event_sort=START_DATE">Data</a></th>
        <th id="event-grid_c3"><a class="sort-link" href="/meus-eventos?Event_sort=ADDRESS">Cidade</a></th>
        <th id="event-grid_c4">Vendidos</th>
        <th id="event-grid_c5">&nbsp;</th>
      </tr>
    </thead>
    <tbody>
      <tr class="odd">
        <td width="57px" style="text-align: center;padding-left:0px;"><span class="" style="display: none;">green</span><img title="Publicado"  src="/images/img-status-green-small.png" /></td><td><a href="/sobre-o-evento?id=182628">Teste</a></td>
        <td width="85px">27/08/2020</td>
        <td width="100px">Evento online</td>
        <td width="174px" class="tickets-sold"><div class="progress-container event-stats" original-title="<div style='color:white;'>Total vendido</div><hr style='margin: 2px 0 7px 0;'><table><tr style='background-color:black; '>
        <td style='padding: 5px;text-align:left;'>Online:</td>
        <td style='padding: 5px;text-align:left;'>R$ 0,00</td></tr></table>" style="width: 100px; display: inline-block;"><div style="width: 66%;"></div><span style="position:relative;top:-21px;left:5px;font-size:12px;">2</span></div> de 3</td>
        <td width="179px" style="text-align: center;padding-left:0px;"><a class="update" title="Editar" href="/editar-evento?id=182628">Editar</a> | <a target="_blank" title="Ir à página" href="https://www.sympla.com.br/teste__182628">Ir à página</a>
        </td>
      </tr>
    </tbody>
    </table>
    <div class="keys" style="display:none" title="/meus-eventos"><span>182628</span></div>
</div>
'''


@pytest.fixture
def response_200():
    response = requests.Response()
    response.status_code = 200
    return response


# http status without 200
@pytest.mark.parametrize("http_status", [
    100, 101, 102,
    201, 202, 203, 204, 205, 206, 207, 208, 226,
    300, 301, 302, 303, 304, 305, 306, 307, 308,
    400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414,
    415, 416, 417, 418, 421, 422, 423, 424, 426, 428, 429, 431, 440, 451,
    500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511
])
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


@pytest.mark.parametrize("http_status", [
    100, 101, 102,
    201, 202, 203, 204, 205, 206, 207, 208, 226,
    300, 301, 302, 303, 304, 305, 306, 307, 308,
    400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414,
    415, 416, 417, 418, 421, 422, 423, 424, 426, 428, 429, 431, 440, 451,
    500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511
])
def test_get_event_failure_raise_exception(monkeypatch, http_status, response_200):
    ''' Raises Exception if http_status is not 200'''
    response = requests.Response()
    response.status_code = http_status

    monkeypatch.setattr('requests.get', mock.MagicMock(return_value=response))
    monkeypatch.setattr('requests.post', mock.MagicMock(return_value=response_200))

    with pytest.raises(Exception, match='Get event failed. Check event id.'):
        sympla = Sympla('email@email.com', '123456')
        sympla.get_event(0)


def test_get_event(monkeypatch, response_200, html_event):
    response = mock.MagicMock(text=html_event, status_code=200)

    monkeypatch.setattr('requests.get', mock.MagicMock(return_value=response))
    monkeypatch.setattr('requests.post', mock.MagicMock(return_value=response_200))

    sympla = Sympla('email@email.com', '123456')
    event = sympla.get_event(1)
    assert event.title == 'Event Test'
    assert event.confirmed_participants == 2
    assert event.pending_participants == 0


def test_get_events(monkeypatch, response_200, html_events):
    response = mock.MagicMock(text=html_events, status_code=200)

    monkeypatch.setattr('requests.get', mock.MagicMock(return_value=response))
    monkeypatch.setattr('requests.post', mock.MagicMock(return_value=response_200))

    sympla = Sympla('email@email.com', '123456')
    event = list(sympla.get_events())[0]
    assert event.title == 'Teste'
