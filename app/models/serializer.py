from flask_marshmallow import Marshmallow
from marshmallow import fields

from app.models.models import User, Account, Post, Comment, Tag

ma = Marshmallow()


def config_ma(app):
    ma.init_app(app)
    return ma


class UserSchema(ma.SQLAlchemyAutoSchema):
    name = fields.String(required=True)
    fone = fields.String()
    email = fields.Email(required=True)

    class Meta:
        model = User
        load_instance = True


class AccountSchema(ma.SQLAlchemyAutoSchema):
    username = fields.String(required=True)
    password = fields.String(required=True)
    user = fields.Nested(UserSchema, only=('id', 'name', 'fone', 'email'))

    class Meta:
        model = Account
        load_instance = True


class PostSchema(ma.SQLAlchemyAutoSchema):
    title = fields.String(required=True)
    content = fields.String(required=True)
    account = fields.Nested(AccountSchema, only=('id', 'username'))

    class Meta:
        model = Post
        load_instance = True


class CommentSchema(ma.SQLAlchemyAutoSchema):
    content = fields.String(required=True)
    post = fields.Nested(PostSchema, only=('id', 'title'))

    class Meta:
        model = Comment
        load_instance = True


class TagSchema(ma.SQLAlchemyAutoSchema):
    name = fields.String(required=True)
    posts = fields.Nested(PostSchema, many=True, only=('id', 'title'))

    class Meta:
        model = Tag
        load_instance = True
