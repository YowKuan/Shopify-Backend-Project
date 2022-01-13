from application import db

has = db.Table('has',
    db.Column('w_id', db.Integer, db.ForeignKey('warehouse.id'), primary_key=True),
    db.Column('i_id', db.Integer, db.ForeignKey('inventory.id'), primary_key=True),
    db.Column('amount', db.Integer)
)

class Warehouse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    address = db.Column(db.String(200))
    capacity = db.Column(db.Integer, nullable=False)
    created_time = db.Column(db.Date)
    
    def __init__(self, name, address, capacity, created_time):
        self.name = name
        self.address = address
        self.capacity = capacity
        self.created_time = created_time
    
    holds = db.relationship('Inventory', secondary=has, lazy='subquery',
        backref=db.backref('warehouse', lazy=True))

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
    