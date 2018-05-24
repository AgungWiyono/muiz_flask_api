import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    # MySQL configurations
    MYSQL_DATABASE_USER = 'default'
    MYSQL_DATABASE_PASSWORD = 'default'
    MYSQL_DATABASE_DB = 'default'
    MYSQL_DATABASE_HOST = 'localhost'