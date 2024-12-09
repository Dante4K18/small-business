from flask import Blueprint, request, jsonify

products_bp = Blueprint('products', __name__)

@products_bp.route('/', methods=['GET'])
def get_products():
    # Importing db and Product here to avoid circular import
    from models import Product, db

    products = Product.query.all()
    return jsonify([{
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'stock_quantity': product.stock_quantity,
        'supplier_id': product.supplier_id
    } for product in products])

@products_bp.route('/', methods=['POST'])
def add_product():
    # Importing db and Product here to avoid circular import
    from models import Product, db

    data = request.get_json()
    new_product = Product(
        name=data['name'],
        description=data.get('description'),
        price=data['price'],
        stock_quantity=data['stock_quantity'],
        supplier_id=data['supplier_id']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product added successfully!'}), 201

@products_bp.route('/<int:id>', methods=['PUT'])
def update_product(id):
    # Importing db and Product here to avoid circular import
    from models import Product, db

    data = request.get_json()
    product = Product.query.get(id)
    if not product:
        return jsonify({'error': 'Product not found!'}), 404
    product.name = data['name']
    product.description = data['description']
    product.price = data['price']
    product.stock_quantity = data['stock_quantity']
    db.session.commit()
    return jsonify({'message': 'Product updated successfully!'})

@products_bp.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    # Importing db and Product here to avoid circular import
    from models import Product, db

    product = Product.query.get(id)
    if not product:
        return jsonify({'error': 'Product not found!'}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully!'})
