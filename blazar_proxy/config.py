"""
Default configuration objects for the application.
"""
import os

class Config(object):
    """
    Base configuration object.
    """
    TESTING = False
    CATS = os.environ.get('CATS', 'defaults/cats.csv')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///database.db')

class ProductionConfig(Config):
    """
    Production configuration object.
    """
    DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///database.db')

class DevelopmentConfig(Config):
    """
    Development configuration object.
    """
    DEBUG = True
    DATABASE_URI = 'sqlite:///database.db'

class TestingConfig(Config):
    """
    Testing configuration object.
    """
    TESTING = True
    DATABASE_URI = 'sqlite:///:memory:'
