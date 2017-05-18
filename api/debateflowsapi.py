#!flask/bin/python
from drivers import users, login
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/v1/users', methods=['GET'], strict_slashes=False)
def get_users():
    (status, data) = users.get_users()
    return jsonify(data), status


@app.route('/v1/users/<int:user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    (status, data) = users.get_user(user_id)
    return jsonify(data), status


@app.route('/v1/users', methods=['POST'], strict_slashes=False)
def new_user():
    (status, data) = users.new_user(request.json)
    return jsonify(data), status

@app.route('/v1/login', methods=['POST'], strict_slashed=False)
def auth_user():
    (status, data) = login.authenticate(request.json)
    return jsonify(data), status

if __name__ == '__main__':
    app.run(host='0.0.0.0')
