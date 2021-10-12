from src.services.AuthService import AuthService


# Example
# @authorize(roles=None) => required token but no roles
# @authorize(roles=['Admin,Staff']) => required token and roles is Admin or Staff
def authorize(roles):
    AuthService.check_auth()
    pass


def get_current_user_id():
    pass


def get_current_role():
    pass
