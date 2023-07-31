"""
Entry point for the application.
"""
from flask import Flask
from werkzeug.utils import import_string
import pandas as pd
from sqlalchemy.exc import NoResultFound
from .model import db, Cat, Vertice
from .views import v1


def create_app(config_filename=''):
    """
    Create a Flask application using the app factory pattern.
    Args:
        config_filename (str): The name of the configuration file to use.
    Returns:
        Flask: The Flask application.
    """
    if not config_filename:
        config_filename = 'ProductionConfig'
    app = Flask(__name__)  # pylint: disable=redefined-outer-name
    config_obj = import_string(f'blazar_proxy.config.{config_filename}')
    app.config.from_object(config_obj)
    # Create database
    db.init_app(app)
    with app.app_context():
        db.create_all()
        cat_df = pd.read_csv("blazar_proxy/defaults/cats.csv")
        vert_df = pd.read_csv("blazar_proxy/defaults/vertices.csv")
        # insert the default cats
        for index, row in cat_df.iterrows():  # pylint: disable=unused-variable
            cat = Cat(id=row['id'], url=row['url'], reference=row['reference'])
            try:
                entry = db.session.query(Cat).filter_by(id=cat.id).one()
            except NoResultFound:
                db.session.add(cat)
                db.session.commit()
                entry = db.session.query(Cat).filter_by(id=cat.id).one()
            # get all the vertices for this cat
            vertices = vert_df[vert_df['cat_id'] == cat.id]
            for index, row in vertices.iterrows():
                vertice = Vertice(name=row['name'], cat_id=entry.id)
                try:
                    entry = db.session.query(Vertice).filter_by(name=vertice.name).one()
                except NoResultFound:
                    db.session.add(vertice)
                    db.session.commit()
    # Register blueprints
    with app.app_context():
        app.register_blueprint(v1.bp)
    return app
