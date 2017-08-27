# pysympla

## Instalação
`pip install pysympla`

## Como Usar
```python
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
```
## Contribuindo
Contribuições são bem-vindas, sinta-se a vontade para abrir uma Issue ou Pull Request
