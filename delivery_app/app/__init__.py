from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
import secrets
# from flask_login import LoginManager
# from datetime import timedelta


app = Flask("Delivery Service")
db_host="terraform-20250508045456317100000001.cpm02wggy33q.us-east-1.rds.amazonaws.com"
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://root:%s@{db_host}/deliverydb" % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)

app.config["SECRET_KEY"] = secrets.token_hex(16)
# app.config["REMEMBER_COOKIE_DURATION"] = timedelta(days=30)
# login = LoginManager(app=app)



