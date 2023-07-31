"""
Database models for the blazar_proxy application.
"""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Cat(db.Model):
    """
    CAT model for the cats table
    """
    id = db.Column(db.String(255), primary_key=True)
    url = db.Column(db.String(255))
    reference = db.Column(db.String(255))

    def __repr__(self):
        return f"<Cat {self.id}>"

class Vertice(db.Model):
    """
    Model for the vertices table
    
    The vertices table contains the vertices (or better known as columns) of the graph.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    cat_id = db.Column(db.Integer, db.ForeignKey('cat.id'), nullable=False)
    cat = db.relationship('Cat', backref=db.backref('columns', lazy=True))

    def __repr__(self):
        return f"<Vertice {self.id}>"
