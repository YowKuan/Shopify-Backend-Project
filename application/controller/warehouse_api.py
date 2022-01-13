from flask_restful import Resource
from flask import Response, request
from datetime import datetime
import json

from application import db
from application.model.model import Warehouse, has, Inventory

class WarehousesAPI(Resource):
    def get(self):
        warehouses = Warehouse.query.order_by(Warehouse.id).all()

        return [{'id': warehouse.id, 
                 'name': warehouse.name, 
                 'capacity':warehouse.capacity,
                 'created_time': str(warehouse.created_time)} for warehouse in warehouses]

    def post(self):
        print(request.data)

        data = request.get_json(force=True)
        print(data)
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        new_warehouse = Warehouse(data['name'], data['address'], data['capacity'], dt_string)
        db.session.add(new_warehouse)
        db.session.commit()
        return "suceess"


class WarehouseAPI(Resource):
    def get(self, id):
        warehouse = Warehouse.query.filter_by(id = id).join(has).join(Inventory).all()
        print(warehouse)
        return warehouse
    
    