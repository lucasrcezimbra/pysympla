import pytest


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
