from flask import Blueprint, request, jsonify
from datetime import datetime

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/', methods=['GET'])
def get_orders():
    # Importing db and models here to avoid circular import
    from models import Order, db
    
    orders = Order.query.all()
    return jsonify([{
        'id': order.id,
        'user_id': order.user_id,
        'product_id': order.product_id,
        'quantity': order.quantity,
        'order_date': order.order_date,
        'status': order.status
    } for order in orders])

@orders_bp.route('/', methods=['POST', 'OPTIONS'])
def create_order():
    from models import Order, Product, User
    from extensions import db
    from datetime import datetime

    data = request.get_json()

    # Validate required fields
    if 'user_id' not in data or 'product_id' not in data or 'quantity' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    if not isinstance(data['quantity'], int) or data['quantity'] <= 0:
        return jsonify({'error': 'Quantity must be a positive integer'}), 400

    # Check if user exists
    user = User.query.get(data['user_id'])
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Check if product exists and has enough stock
    product = Product.query.get(data['product_id'])
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    if product.stock_quantity < data['quantity']:
        return jsonify({'error': 'Insufficient stock!'}), 400

    # Create order and reduce stock
    try:
        product.stock_quantity -= data['quantity']
        new_order = Order(
            user_id=data['user_id'],
            product_id=data['product_id'],
            quantity=data['quantity'],
            order_date=datetime.utcnow(),
            status='pending'
        )
        db.session.add(new_order)
        db.session.commit()

        return jsonify({
            'message': 'Order created successfully!',
            'order': new_order.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An error occurred while creating the order'}), 500
    

@orders_bp.route('/<int:id>', methods=['PUT'])
def update_order_status(id):
    # Importing db and models here to avoid circular import
    from models import Order, db

    data = request.get_json()
    order = Order.query.get(id)
    if not order:
        return jsonify({'error': 'Order not found!'}), 404
    order.status = data['status']
    db.session.commit()
    return jsonify({'message': 'Order status updated successfully!'})
