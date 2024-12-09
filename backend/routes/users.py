from flask import Blueprint, request, jsonify

users_bp = Blueprint('users', __name__)



# Delaying imports to avoid circular import
@users_bp.route('/register', methods=['POST'])
def register_user():
    # Import db and User here to avoid circular import
    from models import User, db  
    
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user:
        return jsonify({'error': 'Email already registered!'}), 400

    new_user = User(
        username=data['username'],
        email=data['email'],
        password=data['password'],
        role=data['role']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully!'}), 201

@users_bp.route('/login', methods=['POST'])
def login_user():
    # Import db and User here to avoid circular import
    from models import User, db

    data = request.get_json()
    user = User.query.filter_by(email=data['email'], password=data['password']).first()
    if not user:
        return jsonify({'error': 'Invalid credentials!'}), 401
    return jsonify({'message': 'Login successful!', 'user_id': user.id, 'role': user.role})



@users_bp.route('/', methods=['GET'])
def get_users():
    from models import User, db
    users = User.query.all()
    return jsonify([{
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'role': user.role
    } for user in users])

# Get user by ID (GET)
@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    from models import User, db
    user = User.query.get(user_id)
    if user:
        return jsonify({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': user.role
        })
    else:
        return jsonify({'error': 'User not found'}), 404