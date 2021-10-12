from cerberus import Validator
from flask_restplus import Resource
from flask import jsonify, make_response, request

from src.utils.ErrorHandle import bad_request
from src.services.LoginService import LoginService
from src.routing import api
# Model vs Schema
from src.validators.LoginSchema import login_schema
from src.models.LoginModel import LoginModel


class CheckLogin(Resource):
    @api.expect(LoginModel.login_model)
    def post(self):
        try:
            # With FormData
            # form = request.form
            json = request.get_json()

            _login_schema = Validator(login_schema)
            if _login_schema.validate(json, login_schema) is False:
                return bad_request(_login_schema.errors)

            LoginService.check_login()
            return make_response(jsonify({"data": "All"}), 200)
        except Exception as error:
            return bad_request(error)
