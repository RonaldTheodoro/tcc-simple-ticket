# Simple Ticket

## Como desenvolver:

1. Clone o repositorio
2. Crie um virtualenv com python 3.6
3. Ative o virtualenv
4. Instale as dependencias
5. Configure a instancia com o .env
6. Execute os testes

```console
git clone https://github.com/RonaldTheodoro/tcc-simple-ticket
cd luizalabs-employee-manager
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```