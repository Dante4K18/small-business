# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# # Initialize Flask app
# app = Flask(__name__)

# # Set up database URI and other configurations
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///business.sqlite3'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # Initialize db and migrate
# db = SQLAlchemy()
# migrate = Migrate(app, db)

# # Import and register blueprints
# from routes.users import users_bp
# from routes.products import products_bp
# from routes.suppliers import suppliers_bp
# from routes.orders import orders_bp

# app.register_blueprint(users_bp, url_prefix='/users')
# app.register_blueprint(products_bp, url_prefix='/products')
# app.register_blueprint(suppliers_bp, url_prefix='/suppliers')
# app.register_blueprint(orders_bp, url_prefix='/orders')

# # Create database tables on first request
# # @app.before_first_request
# # def create_tables():
# #     db.create_all()

# # Test route
# @app.route('/')
# def index():
#     return "Welcome to the Inventory Management System!"

# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask, jsonify
from flask_migrate import Migrate
from extensions import db  # Import the shared db instance
from routes.users import users_bp
from routes.products import products_bp
from routes.suppliers import suppliers_bp
from routes.orders import orders_bp
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

# SQLite Configuration
import os
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///business.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialize Extensions
db.init_app(app)
migrate = Migrate(app, db)


# Import and register blueprints
from routes.users import users_bp
from routes.products import products_bp
from routes.suppliers import suppliers_bp
from routes.orders import orders_bp


# Register Blueprints
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(products_bp, url_prefix='/products')
app.register_blueprint(suppliers_bp, url_prefix='/suppliers')
app.register_blueprint(orders_bp, url_prefix='/orders')

# Define index route
@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Inventory Management System API!"})

if __name__ == "__main__":
    app.run(debug=True)
