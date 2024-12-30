from flask_admin import Admin
from config import app,db
from flask_admin.contrib.sqla import ModelView
from models import Package, BaseUrl
import requests

admin = Admin(app=app)

def get_base_url():
    return BaseUrl.query.get(1).base_url

class PackageModelView(ModelView):
    column_list = ['order_id','state']
    column_editable_list = ['order_id','state']
    edit_modal = True
    create_modal = True
    can_delete = True
    column_filters = ['order_id','state']
    column_searchable_list = ['order_id']

    def after_model_change(self, form, model, is_created):
        if not is_created:
            if 'state' in form:
                if model.state.name != "DELIVERING":
                    url = get_base_url() + "/api/test"
                    body = {
                        'order_id' : model.order_id,
                        'state' : model.state.name,
                    }
                    headers = {
                        "Content-Type": 'application/json',
                    }
                    requests.post(url,json=body,headers=headers)
                
        return super().after_model_change(form, model, is_created)
    

class BaseUrlModelView(ModelView):
    column_list = ['base_url']
    column_editable_list = ['base_url']
    can_delete = False
    can_create = False


admin.add_view(PackageModelView(Package,db.session))
admin.add_view(BaseUrlModelView(BaseUrl,db.session))