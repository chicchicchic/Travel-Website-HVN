from src.routing import api
from src.controllers.RegisterCustomerController import RegisterCustomer


UserRoute = api.namespace('Users', description='')

# POST
UserRoute.add_resource(RegisterCustomer, '/RegisterCustomer')
