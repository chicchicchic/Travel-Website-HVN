import os
from flask import Flask

app = Flask(__name__)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# SQLAlchemy - PostgreSQL URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://internship:hutech@localhost:5432/travel'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# JWT Key
app.config['JWT_SECRET_KEY'] = 'InternHVN'

# Path Image and Extension
app.config['PATH_IMAGE_AVATAR'] = ROOT_DIR + '/src/static/images/users/avatar'
app.config['IMAGE_EXTENSIONS'] = ['PNG', 'JPG', 'JPEG']

# Path templates SendMail
app.config['PATH_SENDMAIL'] = ROOT_DIR + '/src/static/templates/sendmail'

# REST_PLUS Validate Swagger
app.config['RESTPLUS_VALIDATE'] = True
