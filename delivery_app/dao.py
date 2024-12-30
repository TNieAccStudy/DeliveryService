from config import app,db
from models import Package

def add_package(order_id,state):
    package = Package(order_id=order_id,state=state.name)

    db.session.add(package)
    try:
        db.session.commit()
    except Exception as ex:
        return {"err": "fail to attemp add package to data"}, 500
    else:
        return {}, 201