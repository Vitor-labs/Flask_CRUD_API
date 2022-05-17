from flask import Blueprint, current_app, request, jsonify

from ..models.models import Tag
from ..models.serializer import TagSchema
from .auth import validate_jwt


tag = Blueprint('Tag', __name__, url_prefix='/tag')


# Show all tags [GET]
# TESTED - OK
@tag.route('/show', methods=['GET'])
@validate_jwt
def show():
    tag = Tag.query.all()
    schema = TagSchema(many=True)

    return schema.jsonify(tag), 200


# Show one tag [GET]
# TESTED - OK
@tag.route('/show/<int:id>', methods=['GET'])
@validate_jwt
def show_id(id):
    tag = Tag.query.get(id)
    schema = TagSchema()

    return schema.jsonify(tag), 200


# Create a tag [POST]
# TESTED - OK
@tag.route('/create', methods=['POST'])
@validate_jwt
def create():
    data = request.get_json()
    tag = Tag(**data)

    current_app.db.session.add(tag)
    current_app.db.session.commit()

    schema = TagSchema()

    return schema.jsonify(tag), 200


# Update a tagby ID [PATCH]
# TESTING - OK
@tag.route('/edit/<int:id>', methods=['PATCH'])
@validate_jwt
def edit(id):
    tag = Tag.query.get(id)
    data = request.get_json()

    for key, value in data.items():
        setattr(tag, key, value)
    current_app.db.session.commit()

    schema = TagSchema()

    return schema.jsonify(tag), 200


# Delete a tagby ID [DELETE]
# TESTING - OK
@tag.route('/delete/<int:id>', methods=['DELETE'])
@validate_jwt
def delete(id):
    tag = Tag.query.get(id)
    current_app.db.session.delete(tag)
    current_app.db.session.commit()

    return jsonify({'message': 'Tag deleted'}), 200
