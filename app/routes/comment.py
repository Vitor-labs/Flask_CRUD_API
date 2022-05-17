from flask import Blueprint, current_app, request, jsonify

from ..models.models import Comment
from ..models.serializer import CommentSchema
from .auth import validate_jwt


comment = Blueprint('Comment', __name__, url_prefix='/comment')


# Show all comments [GET]
# TESTED - OK
@comment.route('/show', methods=['GET'])
@validate_jwt
def show():
    comment = Comment.query.all()
    schema = CommentSchema(many=True)

    return schema.jsonify(comment), 200


# Show one comment [GET]
# TESTED - OK
@comment.route('/show/<int:id>', methods=['GET'])
@validate_jwt
def show_id(id):
    comment = Comment.query.get(id)
    schema = CommentSchema()

    return schema.jsonify(comment), 200


# Create a comment [POST]
# TESTED - OK
@comment.route('/create', methods=['POST'])
@validate_jwt
def create():
    data = request.get_json()
    comment = Comment(**data)

    current_app.db.session.add(comment)
    current_app.db.session.commit()

    schema = CommentSchema()

    return schema.jsonify(comment), 200


# Update a commentby ID [PATCH]
# TESTING - OK
@comment.route('/edit/<int:id>', methods=['PATCH'])
@validate_jwt
def edit(id):
    comment = Comment.query.get(id)
    data = request.get_json()

    for key, value in data.items():
        setattr(comment, key, value)

    current_app.db.session.commit()

    schema = CommentSchema()

    return schema.jsonify(comment), 200


# Delete a commentby ID [DELETE]
# TESTING - OK
@comment.route('/delete/<int:id>', methods=['DELETE'])
@validate_jwt
def delete(id):
    comment = Comment.query.get(id)
    current_app.db.session.delete(comment)

    return jsonify({'message': 'Comment deleted'}), 200
