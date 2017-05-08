#!flask/bin/python
from drivers import users
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/v1/users', methods=['GET'])
def get_users():
    (status, data) = users.get_users()
    return jsonify(data), status


@app.route('/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    (status, data) = users.get_user(user_id)
    return jsonify(data), status


@app.route('/v1/users', methods=['POST'])
def new_user():
    (status, data) = users.new_user(request.json)
    return jsonify(data), status


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
