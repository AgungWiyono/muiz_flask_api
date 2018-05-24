from app import app
from flask_restful import Resource, Api
from api.User import *

api = Api(app)
api.add_resource(User, '/api/users')

from api import api