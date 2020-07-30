import sqlite3


import data as data
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from models.user import UserModel

from datetime import date
from random import randint
from urllib.parse import quote
import webbrowser

today = date.today()


class UserRegister(Resource):
    TABLE_NAME = 'user_details'

    parser = reqparse.RequestParser()
    parser.add_argument('first_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('last_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('date_of_birth',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('address',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('contact_no',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('qualification',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('gender',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('salary',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('pan_no',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('type_of_employer',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('name_of_employer',
                        type=str,
                        required=True,

                        )

    @jwt_required()
    def get(self, email):
        user = UserModel.find_by_email(email)
        if user:
            return user.json()
        return {'message': 'user not found'}, 404



    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_email(data['email']):
            return {"message": "User with that email id already exists."}, 400
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,NULL,NULL)".format(
            table=self.TABLE_NAME)
        cursor.execute(query, (data['first_name'], data['last_name'], data['date_of_birth'], data['address'], data['contact_no'], data['email'], data['qualification'], data['gender'], data['salary'], data['pan_no'],
                       data['type_of_employer']
                       , data['name_of_employer']))

        connection.close()
        self.update(data['email'])
        connection.commit()

        return {"message": "User created successfully."}, 201

    def update(self, email):

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        salary = cursor.execute("SELECT salary from user_details where user_id='NULL'")
        result = cursor.fetchone()
        for x in result:
            if email == email:
                print(x)

        salary = str(cursor.fetchone())

        print(str(salary))
        # s = str(salary)
        income = (salary * 12)
        salary_per_year = int(income)
        if salary_per_year <= 500000:
            user_type_id = 'A'
        elif salary_per_year > 500000 & salary_per_year <= 1000000:
            user_type_id = 'B'
        elif salary_per_year > 1000000 & salary_per_year <= 1500000:
            user_type_id = 'C'
        elif salary_per_year > 1500000 & salary_per_year <= 3000000:
            user_type_id = 'D'
        elif salary_per_year > 3000000:
            user_type_id = 'E'
        i = 1
        while i > 0:
            num = 1200 + i
        num = num + 1
        user_id = user_type_id + '-' + str(num)
        date = today.strftime("%d")

        month = today.sfrtime("%B")

        random_number = randint(100, 999)
        password = str(date) + str(month) + '-' + str(random_number)

        update_query = "UPDATE user_details set user_id=user_id and password=password where user_id='NULL'"
        cursor.execute(update_query)
        connection.commit()
        connection.close()
        return {'update successfully'}




class UserList(Resource):
      def get(self):
           return {'users': list(map(lambda x: x.json(), UserModel.query.all()))}
