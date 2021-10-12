import datetime
import jwt

from cerberus import Validator
from flask_restplus import Resource
from flask import jsonify, make_response, request
from flask_bcrypt import Bcrypt

from src.utils.ErrorHandle import bad_request
from src.services.LoginService import LoginService
from src.routing import api
from config import app
# Model vs Schema
from src.validators.LoginSchema import LoginSchema
from src.models.LoginModel import LoginModel

bcrypt = Bcrypt(app)


class CheckLogin(Resource):
    @api.expect(LoginModel.login_model)
    def post(self):
        try:
            json = request.get_json()

            schema = LoginSchema.login_schema
            _schema = Validator(schema)
            if _schema.validate(json, schema) is False:
                return bad_request(_schema.errors)

            _username = json['username']
            _password = json['password']

            check = LoginService.check_login(_username)
            if check is not None:

                if check.confirm_email is False:
                    return bad_request('Your account has not activated email')
                elif check.disable is True:
                    return bad_request('Your account has been disabled')

                check_pass = bcrypt.check_password_hash(check.password, _password)
                if check_pass is True:
                    token = jwt.encode({
                        'user_id': str(check.user_id),
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)
                    }, app.config['JWT_SECRET_KEY'], algorithm="HS256")
                    return make_response(jsonify({'token': token}), 200)
                else:
                    return bad_request('Wrong password')

            else:
                return bad_request('Username does not exists')

        except Exception as error:
            return bad_request(error)
