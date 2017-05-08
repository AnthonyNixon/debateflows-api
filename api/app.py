#!flask/bin/python
from drivers import users
from flask import Flask, jsonify

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




if __name__ == '__main__':
    app.run(debug=True)
