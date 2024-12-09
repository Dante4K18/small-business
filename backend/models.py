from datetime import datetime
from extensions import db  # Import `db` from a separate extensions file

# User model: Stores users of the system (either 'admin' or 'employee')
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'admin' or 'employee'

    # Relationship with orders (one-to-many)
    orders = db.relationship('Order', backref='user', lazy=True)


# Product model: Stores information about products in the inventory
class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'), nullable=False)

    # Relationship with orders (one-to-many)
    orders = db.relationship('Order', backref='product', lazy=True)


# Supplier model: Stores suppliers of the products
class Supplier(db.Model):
    __tablename__ = 'suppliers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(255))
    address = db.Column(db.String(255))

    # Relationship with products (one-to-many)
    products = db.relationship('Product', backref='supplier', lazy=True)


# Order model: Stores orders placed by users for specific products
class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Match table name
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)  # Match table name
    quantity = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')
