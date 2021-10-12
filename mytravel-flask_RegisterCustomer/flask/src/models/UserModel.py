from flask_restplus import fields

from src.routing import api


class RegisterCustomerModel:
    register_customer = api.model('Users', {
        'username': fields.String(required=True),
        'password': fields.String(required=True),
        'full_name': fields.String(required=True),
        'email': fields.String(required=True),
        'phone_number': fields.String(required=True),
        'birthday': fields.String(required=True)
    })
