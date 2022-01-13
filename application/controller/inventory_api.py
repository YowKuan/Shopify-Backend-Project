
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
                 'amount': inventory.amount,
                 'not_allocated': inventory.not_allocated} for inventory in Inventories]

    def post(self):
        print(request.data)
        
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

        data = request.get_json(force=True)
        print(data)
        new_inventory = Inventory(data['name'], data['price'], data['amount'], data['amount'], dt_string)
        db.session.add(new_inventory)
        db.session.commit()
        return "success"


class InventoryAPI(Resource):
    def get(self, id):
        inventory = Inventory.query.filter_by(id = id).first()
        print(inventory)
        return inventory
    
    def put(self, id):
        data = request.get_json(force=True)
        inventory = Inventory.query.filter_by(id = id).first()
        inventory.name = data['name']
        inventory.price = data['price']
        inventory.amount = data['amount']
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        inventory.updated_time = dt_string
        db.session.commit()
        return "success"
    
    def delete(self, id):
        inventory = Inventory.query.filter_by(id = id).first()
        db.session.delete(inventory)
        db.session.commit()
        
    
    