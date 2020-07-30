import json
import sqlite3
from random import randint

from flask import request

from flask import Flask, jsonify
from flask_restful import Api

from models.policy import PolicyModel
from models.user import UserModel
from resources.policy import PolicyRegister, PolicyList
from resources.user import UserRegister, today
from resources.user import UserList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'madhu'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api = Api(app)

api.add_resource(UserRegister, '/register')
# api.add_resource(UserRegister, '/user/<string:email>')
# api.add_resource(UserList, '/user/<string:email>')

api.add_resource(UserList, '/users')
api.add_resource(PolicyRegister, '/policyregister')
api.add_resource(PolicyList, '/policies')


@app.route('/user/<string:email>', methods=["DELETE"])
def delete(email):
    user = UserModel.find_by_email(email)
    if user:
        user.delete_from_db()
        return {'message': 'user deleted.'}
    return {'message': 'user not found.'}, 404


@app.route('/policy/<string:policy_name>', methods=["DELETE"])
def delete_policy(policy_name):
    policy = PolicyModel.find_by_policy_name(policy_name)
    if policy:
        policy.delete_to_db()
        return {'message': 'policy deleted.'}
    return {'message': 'policy not found.'}, 404





@app.route("/policy/<string:policy_name>", methods=["GET"])
def policy_detail(policy_name):
    # policy = PolicyModel.query.filter_by(policy_name=policy_name).first_or_404()
    return {'policy': list(map(lambda x: x.json(), PolicyModel.query.filter_by(policy_name=policy_name)))}


@app.route("/policies/<string:company_name>", methods=["GET"])
def policy_detail_by_company(company_name):
    # policy = PolicyModel.query.filter_by(policy_name=policy_name).first_or_404()
    return {'policy': list(map(lambda x: x.json(), PolicyModel.query.filter_by(company_name=company_name)))}


@app.route("/type/<string:policy_type>", methods=["GET"])
def policy_detail_by_type(policy_type):
    return {'policy': list(map(lambda x: x.json(), PolicyModel.query.filter_by(policy_type=policy_type)))}


@app.route("/policy/<int:duration_in_years>", methods=["GET"])
def policy_detail_by_years(duration_in_years):
    return {'policy': list(map(lambda x: x.json(), PolicyModel.query.filter_by(duration_in_years=duration_in_years)))}


# @app.route("/credential/<string:email>", methods=["GET"])


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)