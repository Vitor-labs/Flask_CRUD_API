from flask import Flask
from flask_migrate import Migrate
from .models.models import config_db
from .models.serializer import config_ma


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.db = config_db(app)
    app.ma = config_ma(app)

    Migrate(app, app.db)

    from .routes.user import user
    app.register_blueprint(user)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
