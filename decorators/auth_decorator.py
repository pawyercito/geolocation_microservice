import jwt
from functools import wraps
from flask import jsonify, request, current_app
from app import config

def auth_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token:
            return jsonify({'message': 'Unauthorized'}), 401

        try:
            token = token.replace('Bearer ', '')
            data = jwt.decode(token, config.get('SALT').encode('utf-8'), algorithms=["HS256"])

            # Obtener la información del usuario basada en los datos del token
            user_id = data.get('user_id')
            # Si es necesario, puedes obtener más información del usuario aquí

            # Agregar la información del usuario a los argumentos del controlador
            kwargs['user_id'] = user_id

        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid'}), 401

        return f(*args, **kwargs)

    return decorator
