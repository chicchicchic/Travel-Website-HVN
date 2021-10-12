from src.routing import api
from src.controllers.LoginController import CheckLogin

LoginRoute = api.namespace('Login', description='')

# POST
LoginRoute.add_resource(CheckLogin, '')
