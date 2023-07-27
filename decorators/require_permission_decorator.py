from functools import wraps
from flask import abort, g
from utils.check_permission import check_permission


def require_permission(route):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(g.current_user)
            if not check_permission(g.current_user, route):
                abort(403)  # Opción: Acceso prohibido
            return func(*args, **kwargs)

        return wrapper

    return decorator