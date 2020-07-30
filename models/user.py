from db import db


class UserModel(db.Model):
    __tablename__ = 'user_details'

    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    date_of_birth = db.Column(db.String(80))
    address = db.Column(db.String(100))
    contact_no = db.Column(db.Integer)
    email = db.Column(db.String(80), primary_key=True)
    qualification = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    salary = db.Column(db.Integer)
    pan_no = db.Column(db.String(80))
    type_of_employer = db.Column(db.String(100))
    name_of_employer = db.Column(db.String(100))
    user_id = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, first_name, last_name, date_of_birth, address, contact_no, email, qualification, gender, salary,
                 pan_no, type_of_employer, name_of_employer, user_id, password):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.contact_no = contact_no
        self.email = email
        self.qualification = qualification
        self.gender = gender
        self.salary = salary
        self.pan_no = pan_no
        self.type_of_employer = type_of_employer
        self.name_of_employer = name_of_employer
        self.user_id = user_id
        self.password = password

    def json(self):
        return {'first_name': self.first_name,
                'last_name': self.last_name,
                'date_of_birth': self.date_of_birth,
                'address': self.address,
                'contact_no': self.contact_no,
                'email': self.email,
                'qualification': self.qualification,
                'gender': self.gender,
                'salary': self.salary,
                'pan_no': self.pan_no,
                'type_of_employer': self.type_of_employer,
                'name_of_employer': self.name_of_employer,
                'user_id': self.user_id,
                'password': self.password
                }

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()