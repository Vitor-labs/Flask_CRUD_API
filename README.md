
## How to run this project
- in a linux shell:
```sh
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True

flask run
```
- this is the folder with the __init__ file.
 
 
## How to migrate
```sh
flask db init
flask db migrate
flask db upgrade
```