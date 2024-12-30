from config import app
from flask import redirect, request
import admin
import dao
from models import PackageState

@app.route("/")
def load_index():
    return redirect("/admin")


@app.route("/api/packages/", methods=['post'])
def add_package_to_delivery():
    data = request.json
    order_id = data.get('order_id')
    if order_id>0:
        return dao.add_package(order_id,PackageState.DELIVERING)
    return {"err":"your data not right"},400


if __name__ == "__main__":
    app.run(port=9999,debug=True)