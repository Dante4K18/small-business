from extensions import db
from app import app
from models import User, Product, Supplier, Order
from datetime import datetime

def seed_data():
    with app.app_context():  # Use the app's context to access the db
        db.drop_all()  # Optional: clear the database
        db.create_all()  # Create all tables

        # Seed Users
        users = [
            User(username='admin1', email='admin1@example.com', password='password123', role='admin'),
            User(username='employee1', email='employee1@example.com', password='password123', role='employee')
        ]
        db.session.add_all(users)

        # Seed Suppliers
        suppliers = [
            Supplier(name='Supplier A', contact_info='supplierA@example.com', address='123 Supplier St.'),
            Supplier(name='Supplier B', contact_info='supplierB@example.com', address='456 Supplier Ave.')
        ]
        db.session.add_all(suppliers)

        # Seed Products
        products = [
            Product(name='Product 1', description='Description of Product 1', price=10.99, stock_quantity=50, supplier_id=1),
            Product(name='Product 2', description='Description of Product 2', price=20.99, stock_quantity=30, supplier_id=2)
        ]
        db.session.add_all(products)

        # Seed Orders
        orders = [
            Order(user_id=1, product_id=1, quantity=2, order_date=datetime.utcnow(), status='pending'),
            Order(user_id=2, product_id=2, quantity=1, order_date=datetime.utcnow(), status='completed')
        ]
        db.session.add_all(orders)

        # Commit changes
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_data()
