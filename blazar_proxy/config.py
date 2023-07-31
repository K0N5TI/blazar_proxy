"""
Default configuration objects for the application.
"""
import os

class Config(object):  # pylint: disable=too-few-public-methods,useless-object-inheritance
    """
    Base configuration object.
    """
    TESTING = False
    CATS = os.environ.get('CATS', 'defaults/cats.csv')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///database.db')

class ProductionConfig(Config):  # pylint: disable=too-few-public-methods
    """
    Production configuration object.
    """
    DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///database.db')

class DevelopmentConfig(Config):  # pylint: disable=too-few-public-methods
    """
    Development configuration object.
    """
    DEBUG = True
    DATABASE_URI = 'sqlite:///database.db'

class TestingConfig(Config):  # pylint: disable=too-few-public-methods
    """
    Testing configuration object.
    """
    TESTING = True
    DATABASE_URI = 'sqlite:///:memory:'
