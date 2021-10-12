from flask_restplus import fields

from src.routing import api


class LoginModel:
    # With Json
    login_model = api.model('Login', {
        'Email': fields.String(required=True),
        'Password': fields.String(required=True)
    })
