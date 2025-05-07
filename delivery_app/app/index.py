from app import app
from flask import redirect, request
from app import dao,admin
from app.models import PackageState

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
    app.run(host="0.0.0.0", port=7300,debug=True)
