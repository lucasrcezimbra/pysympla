pysympla
============
.. image:: https://badge.fury.io/py/pysympla.svg
    :target: https://badge.fury.io/py/pysympla
.. image:: https://travis-ci.org/Lrcezimbra/pysympla.svg?branch=master
    :target: https://travis-ci.org/Lrcezimbra/pysympla
.. image:: https://coveralls.io/repos/github/Lrcezimbra/pysympla/badge.svg?branch=master
    :target: https://coveralls.io/github/Lrcezimbra/pysympla?branch=master
.. image:: https://landscape.io/github/Lrcezimbra/pysympla/master/landscape.svg?style=flat-square
    :target: https://landscape.io/github/Lrcezimbra/pysympla/master
    :alt: Code Health
.. image:: https://pyup.io/repos/github/Lrcezimbra/pysympla/shield.svg
    :target: https://pyup.io/repos/github/Lrcezimbra/pysympla/
    :alt: Updates


Instalação
~~~~~~~~~~~~~
``pip install pysympla``


Como Usar
~~~~~~~~~~~~~
.. code-block:: python

    from pysympla import Sympla

    # Autenticação
    sympla = Sympla('username', 'password')

    # Retorna evento especifíco
    event = sympla.get_event('ID')
    print(event.title, event.confirmed_participants, event.pending_participants)

    # Retorna generator de eventos
    events = sympla.get_events()
    for event in events:
        print(event.title, event.confirmed_participants, event.pending_participants)


Contribuindo
~~~~~~~~~~~~~
Contribuições são bem-vindas, sinta-se a vontade para abrir uma Issue ou Pull Request
