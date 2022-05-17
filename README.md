# API FOR TWITER SCRAPING (IN DEVELOPMENT)

## Tech Stack

**Client:** *IN PRODUCTION*

**Server:** Flask, Python, Marshmallow

 - **Database:** Alembic, SQLite, SQLAlchemy

## Falta Fazer:
- Autentificar as rotas
- gerar hash das senhas
- criar testes com o Fazer
- criar instancia do server
- migrar o banco e seeders
- adicionar loggers


## How to run this project
- on linux:
```sh
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True

flask run
```
- on windows:
```cmd
set FLASK_APP=app
set FLASK_ENV=Development
set FLASK_DEBUG=True

flask run
```


## How to migrate
```sh
flask db init
flask db migrate
flask db upgrade
```