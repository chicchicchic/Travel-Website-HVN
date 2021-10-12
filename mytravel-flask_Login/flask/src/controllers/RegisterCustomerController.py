from flask_bcrypt import Bcrypt
from cerberus import Validator
from flask_restplus import Resource
from flask import jsonify, make_response, request

from src.models.UserModel import RegisterCustomerModel
from src.routing import api
from src.services.UserService import UserService
from src.utils.ErrorHandle import bad_request
from src.validators.RegisterCustomerSchema import RegisterCustomerSchema
from config import app

bcrypt = Bcrypt(app)


class RegisterCustomer(Resource):
    @api.expect(RegisterCustomerModel.register_customer)
    def post(self):
        try:
            json = request.get_json()

            schema = RegisterCustomerSchema.reg_customer_schema
            _schema = Validator(schema)
            if _schema.validate(json, schema) is False:
                return bad_request(_schema.errors)

            username = json['username']
            full_name = json['full_name']
            email = json['email']
            phone_number = json['phone_number']
            birthday = json['birthday']
            password = bcrypt.generate_password_hash(json['password']).decode('utf-8')

            reg_customer = UserService.register_customer(username, password, full_name, email, phone_number, birthday)

            if reg_customer is True:
                return make_response("true", 201)
            elif str(reg_customer).find('unique_username') != -1:
                return bad_request("Username already exists")
            elif str(reg_customer).find('unique_email') != -1:
                return bad_request("Email already exists")
            elif str(reg_customer).find('unique_phone_number') != -1:
                return bad_request("Phone number already exists")
        except Exception as error:
            return bad_request(error.args)
