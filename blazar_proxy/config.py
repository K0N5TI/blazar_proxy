import os

class Config(object):
    TESTING = False
    CATS = os.environ.get('CATS', 'defaults/cats.csv')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///database.db')

class ProductionConfig(Config):
    DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///database.db')

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = 'sqlite:///database.db'

class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = 'sqlite:///:memory:'