# API FOR TWITER SCRAPING (IN DEVELOPMENT)

## Tech Stack

**Client:** *IN PRODUCTION*

**Server:** Flask, Python, Marshmallow

 - **Database:** Alembic, SQLite, SQLAlchemy

## How to run this project
- in a linux shell:
```sh
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True

flask run
```
- in windows:
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