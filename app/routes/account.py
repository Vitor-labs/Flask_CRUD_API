from flask import Blueprint, current_app, request, jsonify

from ..models.models import Account
from ..models.serializer import AccountSchema

account = Blueprint('Account', __name__, url_prefix='/account')


# Show all accounts [GET]
# TESTED - OK
@account.route('/show', methods=['GET'])
def show():
    account = Account.query.all()
    schema = AccountSchema(many=True)

    return schema.jsonify(account), 200


# Show one account [GET]
# TESTED - OK

@account.route('/show/<int:id>', methods=['GET'])
def show_id(id):
    account = Account.query.get(id)
    schema = AccountSchema()

    return schema.jsonify(account), 200


# Create a account [POST]
# TESTED - OK
@account.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    account = Account(**data)

    current_app.db.session.add(account)
    current_app.db.session.commit()

    schema = AccountSchema()

    return schema.jsonify(account), 200


# Update a accountby ID [PATCH]
# TESTING - OK
@account.route('/edit/<int:id>', methods=['PATCH'])
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
def delete(id):
    account = Account.query.get(id)
    current_app.db.session.delete(account)
    current_app.db.session.commit()

    return jsonify({'message': 'Account deleted'}), 200
