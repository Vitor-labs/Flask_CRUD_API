from flask import current_app, request, jsonify, Response
import jwt
from functools import wraps


def validate_jwt(f) -> Response:
    @wraps(f)
    def decorated(*args, **kwargs):
        print('validating token')
        token = request.headers.get('Authorization')
        if token:
            token = token.split(' ')[1]

            try:
                data = jwt.decode(
                    token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
                print(data)
            except Exception as e:
                print(e)
                return jsonify({'message': 'Token is invalid'}), 401
        else:
            return jsonify({'message': 'Token is missing'}), 401

        return f(*args, **kwargs)
    return decorated
