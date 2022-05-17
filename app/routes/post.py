from flask import Blueprint, current_app, request, jsonify

from ..models.models import Post
from ..models.serializer import PostSchema
from .auth import validate_jwt


post = Blueprint('Post', __name__, url_prefix='/post')


# Show all posts [GET]
# TESTED - OK
@post.route('/show', methods=['GET'])
@validate_jwt
def show():
    post = Post.query.all()
    schema = PostSchema(many=True)

    return schema.jsonify(post), 200


# Show one post [GET]
# TESTED - OK
@post.route('/show/<int:id>', methods=['GET'])
@validate_jwt
def show_id(id):
    post = Post.query.get(id)
    schema = PostSchema()

    return schema.jsonify(post), 200


# Create a post [POST]
# TESTED - OK
@post.route('/create', methods=['POST'])
@validate_jwt
def create():
    data = request.get_json()
    post = Post(**data)

    current_app.db.session.add(post)
    current_app.db.session.commit()

    schema = PostSchema()

    return schema.jsonify(post), 200


# Update a postby ID [PATCH]
# TESTING - OK
@post.route('/edit/<int:id>', methods=['PATCH'])
@validate_jwt
def edit(id):
    post = Post.query.get(id)
    data = request.get_json()

    for key, value in data.items():
        setattr(post, key, value)
    current_app.db.session.commit()

    schema = PostSchema()

    return schema.jsonify(post), 200


# Delete a postby ID [DELETE]
# TESTING - OK
@post.route('/delete/<int:id>', methods=['DELETE'])
@validate_jwt
def delete(id):
    post = Post.query.get(id)
    current_app.db.session.delete(post)

    return jsonify({'message': 'Post deleted'}), 200
