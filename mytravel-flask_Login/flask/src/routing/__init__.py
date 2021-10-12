from flask_restplus import Api
from werkzeug.middleware.proxy_fix import ProxyFix
from config import app

security = [
    {
        "api_key": []
    }
]

authorizations = {
    "api_key": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization",
        "scheme": "bearer",
        "bearerFormat": "JWT"
    }
}

app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0.0', title='Travel API', doc='/',
          description='',
          authorizations=authorizations)

from src.routing.UserRoute import UserRoute
from src.routing.LoginRoute import LoginRoute
