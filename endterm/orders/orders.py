from flask import Flask, jsonify, request
from flask_cors import CORS
from models import Order, db
import requests
from sqlalchemy.exc import IntegrityError
import os
import json
import jwt

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, '../data/orders.db')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:////' + db_path)

db.init_app(app)

PRODUCTS_SERVICE_URL = "http://products:5001"
AUTH_SERVICE_URL = "http://auth:5000"

SECRET_KEY = '32f7d11a6d4ab32c2ad57029f1c42b13e02e2707b4e3f30a4f1e3f4853a731e3'

def validate_token(token):
    try:
        response = requests.post(f"{AUTH_SERVICE_URL}/validate_token", json={"token": token})
        response.raise_for_status()
        print(response)
        return True if response.json().get("valid") else False
    except requests.exceptions.RequestException as e:
        print(f"Error validating token: {e}")
        return False

@app.route('/create_order', methods=['POST'])
def create_order():
    token = request.headers.get('Authorization')
    if token and token.startswith('Bearer '):
        token = token[7:] 
    if not token:
        return jsonify({"message": "Token is missing"}), 401

    if not validate_token(token):
        return jsonify({"message": "Invalid token"}), 401

    try:
        token_data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_id = token_data['username']
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token here"}), 401  

    data = request.get_json()
    items = data.get('items', [])

    if not isinstance(items, list) or not all(isinstance(item, dict) for item in items):
        return jsonify({'message': 'Invalid format for items'}), 400

    total_price = 0
    product_ids = []
    products_details = {}

    for item in items:
        product_id = item.get('product_id')
        quantity = item.get('quantity')

        if quantity is None:
            return jsonify({'message': 'Quantity is required for each item'}), 400

        product_ids.append(product_id)

        product_details_response = requests.get(f"{PRODUCTS_SERVICE_URL}/products/{product_id}")

        if product_details_response.status_code != 200:
            return jsonify({'message': f'Product with ID {product_id} not found'}), 404

        product_details = product_details_response.json()
        products_details[product_id] = product_details

        item_price = product_details['price'] * quantity
        total_price += item_price

        new_order = Order(user_id=user_id, total_price=total_price, quantity=quantity)
        db.session.add(new_order)
    try:
        db.session.commit()
        return jsonify({'message': 'Order created successfully', 'total_price': total_price, 'product_ids': product_ids, 'products': product_details}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Order creation failed. Duplicate order.'}), 400

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5002)
