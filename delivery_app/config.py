from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
import secrets
# from flask_login import LoginManager
# from datetime import timedelta


app = Flask("Delivery Service")

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/deliverydb" % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)

app.config["SECRET_KEY"] = secrets.token_hex(16)
# app.config["REMEMBER_COOKIE_DURATION"] = timedelta(days=30)
# login = LoginManager(app=app)



