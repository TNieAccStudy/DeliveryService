from config import db,app
from sqlalchemy import INTEGER,FLOAT,String,Column,ForeignKey,BOOLEAN,DATETIME,Enum
from enum import Enum as EnumClass
# from flask_login import UserMixin
import hashlib
from datetime import datetime as dt

# class User(UserMixin, db.Model):
#     __tablename__ = "users"
#     id = Column(INTEGER,primary_key=True,autoincrement=True)
#     username = Column(String(50),nullable=False)
#     password = Column(String(255),nullable=False)


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(INTEGER,primary_key=True,autoincrement=True)
    active = Column(BOOLEAN,default=True)
    created_date = Column(DATETIME,default=dt.now())
    updated_date = Column(DATETIME,default=dt.now(), onupdate=dt.now())

class BaseUrl(db.Model):
    id = Column(INTEGER,primary_key=True,autoincrement=True)
    base_url = Column(String(255),nullable=False)


class PackageState(EnumClass):
    DELIVERING = 1
    SUCCESS = 2
    CLIENTNOTRECEIVE = 3
    DELIVERYPROBLEM = 4


class Package(BaseModel):
    __tablename__ = "packages"
    id = Column(INTEGER, primary_key=True,autoincrement=True)
    order_id = Column(INTEGER,nullable=False,unique=True)
    state = Column(Enum(PackageState), default=PackageState.DELIVERING)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        # admin = User(username="admin",password=hashlib.md5('123456'.strip().encode("utf-8")).hexdigest())

        # db.session.add(admin)


        db.session.add(BaseUrl(base_url="http://127.0.0.1:5000"))
        db.session.commit()

        # db.session.commit()