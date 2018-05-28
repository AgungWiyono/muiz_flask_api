from app import app
from flask_restful import Resource, Api
from model.User import UserApi
from model.Post import PostApi

api = Api(app)
api.add_resource(UserApi, '/api/users')
api.add_resource(PostApi, '/api/posts')

from api import api