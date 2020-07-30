import sqlite3

from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from models.policy import PolicyModel


class PolicyRegister(Resource):
    TABLE_NAME = 'policy_table'

    parser = reqparse.RequestParser()

    parser.add_argument('policy_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('start_date',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('duration_in_years',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('company_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('initial_deposit',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('policy_type',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('user_type',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('terms_per_year',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('term_amount',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('interest',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    @jwt_required()
    def get(self, policy_name):
        policy = PolicyModel.find_by_policy_name(policy_name)
        if policy:
            return policy.json()
        return {'message': 'policy not found'}, 404

    @jwt_required()
    def get(self, company_name):
        policy = PolicyModel.find_by_company_name(company_name)
        if policy:
            return policy.json()
        return {'message': 'policy not found'}, 404


    @jwt_required
    def get_type(self, policy_type):
        policy = PolicyModel.find_by_policy_type(policy_type)
        if policy:
            return policy.json()
        return {'message': 'policy not found'}, 404

    @jwt_required
    def get_years(self, duration_in_years):
        policy = PolicyModel.find_by_years(duration_in_years)
        if policy:
            return policy.json()
        return {'message': 'policy not found'}, 404

    def post(self):
        data = PolicyRegister.parser.parse_args()

        connection = sqlite3.connect('data.db')
       # connection2 = sqlite3.connect('data.db')
        cursor = connection.cursor()
        #cursor2 = connection2.cursor()
        query = "INSERT INTO {table} VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?,NULL,NULL)".format(table=self.TABLE_NAME)
        cursor.execute(query, (data['policy_name'], data['start_date'], data['duration_in_years'], data['company_name'], data['initial_deposit'], data['policy_type'], data['user_type'], data['terms_per_year'], data['term_amount'], data['interest']))
        connection.commit()
        connection.close()

        return {"message": "Policy created successfully."}, 201


class PolicyList(Resource):
    def get(self):
        return {'policies': list(map(lambda x: x.json(), PolicyModel.query.all()))}


