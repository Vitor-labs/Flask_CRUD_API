from flask import Blueprint, current_app, request, jsonify

from ..models.models import User
from ..models.serializer import UserSchema

user = Blueprint('User', __name__, url_prefix='/user')


@user.route('/show', methods=['GET'])
def show():
    user = User.query.all()
    schema = UserSchema(many=True)

    return schema.jsonify(user), 200


@user.route('/show/<int:id>', methods=['POST'])
def show_id(id):
    user = User.query.get(id)
    schema = UserSchema()

    return schema.jsonify(user), 200


@user.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    user = User(**data)

    current_app.db.session.add(user)
    current_app.db.session.commit()

    schema = UserSchema()

    return schema.jsonify(user), 200


@user.route('/edit/<int:id>', methods=['PUT'])
def edit(id):
    user_schema = UserSchema()
    query = User.query.filter(User.id == id).first()
    query.update(request.json)

    current_app.db.session.commit()
    return user_schema.jsonify(query), 200


@user.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    user = User.query.get(id)
    current_app.db.session.delete(user)
    current_app.db.session.commit()

    return jsonify({'message': 'User deleted'}), 200
