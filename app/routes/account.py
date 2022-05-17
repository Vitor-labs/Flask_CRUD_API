import datetime
import jwt
from flask import Blueprint, current_app, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from ..models.models import Account
from ..models.serializer import AccountSchema
from .auth import validate_jwt

account = Blueprint('Account', __name__, url_prefix='/account')


# Return a JWT token for the user/account [GET]
# Tested - OK
@account.route('/login', methods=['GET'])
def authorization():
    """
    you have to use a account an account already created
    """
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Authentication failed'}), 401

    account = Account.query.filter_by(username=auth.username).first()

    if not account:
        return jsonify({'message': 'User not found'}), 404

    if account and check_password_hash(account.password, auth.password):
        token = jwt.encode({
            'user': account.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, current_app.config['SECRET_KEY'])

        return jsonify({'message': 'Authentication successful',
                        'token': token,
                        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)})
    else:
        return jsonify({'message': 'Authentication failed'}), 401


# Show all accounts [GET]
# TESTED - OK
@account.route('/show', methods=['GET'])
@validate_jwt
def show():
    account = Account.query.all()
    schema = AccountSchema(many=True)

    return schema.jsonify(account), 200


# Show one account [GET]
# TESTED - OK
@account.route('/show/<int:id>', methods=['GET'])
@validate_jwt
def show_id(id):
    account = Account.query.get(id)
    schema = AccountSchema()

    return schema.jsonify(account), 200


# Create a account [POST]
# TESTED - OK
@account.route('/create', methods=['POST'])
@validate_jwt
def create():
    data = request.get_json()
    account = Account(**data)

    hash_pass = generate_password_hash(account.password)
    account.password = hash_pass

    current_app.db.session.add(account)
    current_app.db.session.commit()

    schema = AccountSchema()

    return schema.jsonify(account), 200


# Update a accountby ID [PATCH]
# TESTING - OK
@account.route('/edit/<int:id>', methods=['PATCH'])
@validate_jwt
def edit(id):
    account = Account.query.get(id)
    data = request.get_json()

    for key, value in data.items():
        setattr(account, key, value)
    current_app.db.session.commit()

    schema = AccountSchema()

    return schema.jsonify(account), 200


# Delete a account by ID [DELETE]
# TESTED - OK
@account.route('/delete/<int:id>', methods=['DELETE'])
@validate_jwt
def delete(id):
    account = Account.query.get(id)
    current_app.db.session.delete(account)
    current_app.db.session.commit()

    return jsonify({'message': 'Account deleted'}), 200
