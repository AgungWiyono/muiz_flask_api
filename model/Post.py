from datetime import datetime
from flask_restful import Resource, reqparse
from db import db
from model.User import UserDAO

class PostApi(Resource):
    def get(self):
        return {'hello':'posts'}
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('body', type=str, help='body of post')

        args = parser.parse_args()
        body = args['body']

        u = UserDAO.query.get(1)
        post = PostDAO(body=body, author=u)
        db.session.add(post)
        db.session.commit()
        
        return {'success': 'success'}

class PostDAO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(180))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('userDAO.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

    