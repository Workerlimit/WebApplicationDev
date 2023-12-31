from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from models import Base, User
from sqlalchemy.orm import scoped_session, sessionmaker
import bcrypt
import jwt
from sqlalchemy.orm import declarative_base
import os

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE,OPTIONS'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, '../data/auth.db')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///' + db_path)

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Base.metadata.create_all(engine)

Session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

SECRET_KEY = '32f7d11a6d4ab32c2ad57029f1c42b13e02e2707b4e3f30a4f1e3f4853a731e3'

@app.route('/')
def home():
    return 'Authentication Microservice is up and running!'

@app.route('/validate_token', methods=['POST'])
def validate_token():
    data = request.get_json()
    token = data.get('token')

    if not token:
        return jsonify({"valid": False, "message": "Token is missing"}), 401

    try:
        jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return jsonify({"valid": True, "message": "Token is valid"}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({"valid": False, "message": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"valid": False, "message": "Invalid token"}), 401

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Both username and password are required'}), 400

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    new_user = User(username=username, password=hashed_password)
    with Session() as session:
        session.add(new_user)
        try:
            session.commit()
            session.close()
            return jsonify({'message': 'User registered successfully'}), 201
        except IntegrityError:
            session.rollback()
            session.close()
            return jsonify({'message': 'Username is already in use. Please choose another.'}), 400

@app.route('/signin', methods=['POST'])
def signin():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Both username and password are required'}), 400

    with Session() as session:
        user = session.query(User).filter_by(username=username).first()
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            token = jwt.encode({'username': username}, SECRET_KEY, algorithm='HS256')
            session.close()
            return jsonify({'message': 'Sign-in successful', 'token': token}), 200
        else:
            session.close()
            return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
