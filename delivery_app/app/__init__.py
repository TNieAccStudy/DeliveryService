from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
import secrets
# from flask_login import LoginManager
# from datetime import timedelta


app = Flask("Delivery Service")
db_host="terraform-20250508140112104500000001.ct826iweg6n5.us-east-1.rds.amazonaws.com"
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://admin:%s@{db_host}/deliverydb" % quote('admin1234')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)

app.config["SECRET_KEY"] = secrets.token_hex(16)
# app.config["REMEMBER_COOKIE_DURATION"] = timedelta(days=30)
# login = LoginManager(app=app)



