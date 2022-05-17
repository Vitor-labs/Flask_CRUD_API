from flask import Flask
from flask_migrate import Migrate

from .conf import key
from .models.models import config_db
from .models.serializer import config_ma


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = key # Everytime the server is restarted, the key changes

    app.db = config_db(app)
    app.ma = config_ma(app)

    Migrate(app, app.db)

    # Routes Registration on main server
    from .routes.account import account
    from .routes.comment import comment
    from .routes.post import post
    from .routes.tag import tag
    from .routes.user import user

    app.register_blueprint(account)
    app.register_blueprint(comment)
    app.register_blueprint(post)
    app.register_blueprint(tag)
    app.register_blueprint(user)
    # ==================================

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
