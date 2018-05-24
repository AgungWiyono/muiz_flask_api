from flask_restful import Resource, reqparse
from api.JsonReturn import JsonReturn
from db import mysql

def map_sql_error(obj):
    return str(obj[0])

class User(Resource):
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

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('spCreateUser',(_userName, _userEmail, _userPassword))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                data =  {
                        'name': _userName,
                        'email': _userEmail
                    }
                return JsonReturn.success(data, 201)
            else:
                msg = list(map(map_sql_error, data))
                return JsonReturn.fail(msg)

        except Exception as e:
            return JsonReturn.error(str(e))
        