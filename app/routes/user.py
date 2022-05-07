from flask import Blueprint, current_app, request, jsonify

from ..models.models import User
from ..models.serializer import UserSchema

user = Blueprint('User', __name__, url_prefix='/user')

# Show all users [GET]
# TESTED - OK
@user.route('/show', methods=['GET'])
def show():
    user = User.query.all()
    schema = UserSchema(many=True)

    return schema.jsonify(user), 200

# Show one user [GET]
# TESTED - OK
@user.route('/show/<int:id>', methods=['GET'])
def show_id(id):
    user = User.query.get(id)
    schema = UserSchema()

    return schema.jsonify(user), 200

# Create a user [POST]
# TESTED - OK
@user.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    user = User(**data)

    current_app.db.session.add(user)
    current_app.db.session.commit()

    schema = UserSchema()

    return schema.jsonify(user), 200


# Update a userby ID [PATCH]
# TESTING - OK
@user.route('/edit/<int:id>', methods=['PATCH'])
def edit(id):
    user = User.query.get(id)
    data = request.get_json()

    for key, value in data.items():
        setattr(user, key, value)
    current_app.db.session.commit()

    schema = UserSchema()

    return schema.jsonify(user), 200


# Delete a user by ID [DELETE]
# TESTED - OK
@user.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    user = User.query.get(id)
    current_app.db.session.delete(user)
    current_app.db.session.commit()

    return jsonify({'message': 'User deleted'}), 200
