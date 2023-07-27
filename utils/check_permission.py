from models.permission_role.permission_role_model import Permission


def check_permission(user, route):
    if not user:
        return False
    return Permission.query.filter_by(role_id=user.role_id, route=route).first() is not None
