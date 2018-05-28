from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
from api import api
from model.User import UserDAO

# app.run(host='0.0.0.0', port=1997, debug=True)