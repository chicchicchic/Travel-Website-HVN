from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from config import app

db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)

# Database First
# Tables
login = Base.classes.login
user_info = Base.classes.user_info
role = Base.classes.role
