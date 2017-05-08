#!flask/bin/python
from drivers import users
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/v1/users', methods=['GET'])
def get_users():
    return jsonify(users.get_users())


@app.route('/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify(users.get_user(user_id))


@app.route('/v1/users', methods=['POST'])
def new_user():
    return jsonify(users.new_user(request.json))


if __name__ == '__main__':
    app.run(debug=True)
