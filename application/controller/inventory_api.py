
from flask_restful import Resource
from flask import Response, request
from datetime import datetime
import json

from application import db
from application.model.model import Inventory

class InventoriesAPI(Resource):
    def get(self):
        Inventories = Inventory.query.order_by(Inventory.id).all()

        return [{'id': inventory.id, 
                 'name': inventory.name, 
                 'price':inventory.price,
                 'amount': inventory.amount} for inventory in Inventories]

    def post(self):
        print(request.data)

        data = request.get_json(force=True)
        print(data)
        new_warehouse = Inventory(data['name'], data['price'], data['amount'])
        db.session.add(new_warehouse)
        db.session.commit()
        return "suceess"


class InventoryAPI(Resource):
    def get(self, id):
        warehouse = Inventory.query.filter_by(id = id).first()
        print(warehouse)
        return warehouse
    
    def put(self, id):
        data = request.get_json(force=True)
        warehouse = Inventory.query.filter_by(id = id).first()
        warehouse.name = data['name']
        warehouse.price = data['price']
        warehouse.amount = data['amount']
        db.session.commit()
        return "success"
    
    def delete(self, id):
        warehouse = Inventory.query.filter_by(id = id).first()
        db.session.delete(warehouse)
        db.session.commit()
        
    
    