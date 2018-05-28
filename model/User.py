from flask_restful import Resource, reqparse
from api.JsonReturn import JsonReturn
from db import db

def map_sql_error(obj):
    return str(obj[0])

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserApi(Resource):
    def get(self):
        return {'Hello':'World'}

    def post(self):
        try:
            parser = reqparse.RequestParser()        
            parser.add_argument('name', type=str, help='Name for new User')
            parser.add_argument('email', type=str, help='Email address to create user')
            parser.add_argument('password', type=str, help='Password to create user')

            args = parser.parse_args()
            _userName = args['name']
            _userEmail = args['email']
            _userPassword = args['password']

            if _userName is None:
                return JsonReturn.fail('name can\'t empty')
            if _userEmail is None:
                return JsonReturn.fail('email can\'t empty')
            if _userPassword is None:
                return JsonReturn.fail('password can\'t empty')

            new_user = UserDAO(name=_userName, email=_userEmail, password=_userPassword)
            db.session.add(new_user)
            db.session.commit()
            data =  {
                'name': _userName,
                'email': _userEmail
            }
            return JsonReturn.success(data, 201)

        except Exception as e:
            return JsonReturn.error(str(e))

class UserDAO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    posts = db.relationship('PostDAO', backref='author', lazy='dynamic')

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password