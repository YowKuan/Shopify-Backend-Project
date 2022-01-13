from flask import Blueprint, render_template
from flask import current_app as app
from application.controller.warehouse_api import WarehousesAPI, WarehouseAPI

API_warehouses = WarehousesAPI()
API_warehouse = WarehouseAPI()

# Blueprint Configuration
warehouse_bp = Blueprint(
    'warehouse_bp', __name__,
    template_folder='templates',
    url_prefix='/warehouses'
)


@warehouse_bp.route('/', methods=['GET'])
def warehouses():
    """Homepage."""
    
    warehouses = API_warehouses.get()
    print(warehouses)
    return render_template(
        'warehouses.html',
        warehouses = warehouses
    )
@warehouse_bp.route('/<id>', methods=['GET'])
def warehouse():
    warehouse_info = API_warehouse.get()
    return render_template(
        'warehouse.html',
        warehouse_info = warehouse_info
        
    )
