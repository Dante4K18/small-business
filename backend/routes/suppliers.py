from flask import Blueprint, request, jsonify
# from extensions import db
# from models import Supplier
suppliers_bp = Blueprint('suppliers', __name__)

def success_response(message, data=None, status_code=200):
    """Generate a success response."""
    response = {'message': message}
    if data:
        response['data'] = data
    return jsonify(response), status_code

def error_response(error_message, status_code=400):
    """Generate an error response."""
    return jsonify({'error': error_message}), status_code


@suppliers_bp.route('/', methods=['GET'])
def get_suppliers():
    from models import Supplier
    """Fetch all suppliers."""
    try:
        suppliers = Supplier.query.all()
        supplier_list = [
            {
                'id': supplier.id,
                'name': supplier.name,
                'contact_info': supplier.contact_info,
                'address': supplier.address
            }
            for supplier in suppliers
        ]
        return success_response("Suppliers retrieved successfully!", supplier_list)
    except Exception as e:
        return error_response(f"Failed to retrieve suppliers: {str(e)}", 500)


@suppliers_bp.route('/', methods=['POST'])
def add_supplier():
    from extensions import db
    from models import Supplier
    """Add a new supplier."""
    data = request.get_json()

    # Validate required fields
    if not data or not all(data.get(key) for key in ('name', 'contact_info', 'address')):
        return error_response("Missing required fields: name, contact_info, and address", 400)

    try:
        new_supplier = Supplier(
            name=data['name'],
            contact_info=data['contact_info'],
            address=data['address']
        )
        db.session.add(new_supplier)
        db.session.commit()
        return success_response("Supplier added successfully!", {'supplier_id': new_supplier.id}, 201)
    except Exception as e:
        return error_response(f"Failed to add supplier: {str(e)}", 500)


@suppliers_bp.route('/<int:id>', methods=['PUT'])
def update_supplier(id):
    from models import Supplier
    from extensions import db
    """Update an existing supplier."""
    data = request.get_json()

    try:
        supplier = Supplier.query.get(id)
        if not supplier:
            return error_response("Supplier not found!", 404)

        # Validate required fields
        if not data or not all(data.get(key) for key in ('name', 'contact_info', 'address')):
            return error_response("Missing required fields: name, contact_info, and address", 400)

        supplier.name = data['name']
        supplier.contact_info = data['contact_info']
        supplier.address = data['address']
        db.session.commit()

        return success_response("Supplier updated successfully!")
    except Exception as e:
        return error_response(f"Failed to update supplier: {str(e)}", 500)


@suppliers_bp.route('/<int:id>', methods=['DELETE'])
def delete_supplier(id):
    from models import Supplier
    from extensions import db
    """Delete a supplier."""
    try:
        supplier = Supplier.query.get(id)
        if not supplier:
            return error_response("Supplier not found!", 404)

        db.session.delete(supplier)
        db.session.commit()
        return success_response("Supplier deleted successfully!")
    except Exception as e:
        return error_response(f"Failed to delete supplier: {str(e)}", 500)
