from flask_restplus import fields

from src.routing import api


class LoginModel:
    login_model = api.model('Login', {
        'username': fields.String(required=True),
        'password': fields.String(required=True)
    })
