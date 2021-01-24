from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass


db = SQLAlchemy()

@dataclass # see: https://docs.python.org/3.8/library/dataclasses.html
class Discount(db.Model):
    """ Class for modelling a basic discount database entity """
    code: str
    brand: str
    user: str

    code = db.Column(db.String(10), primary_key=True)
    brand = db.Column(db.String(20), unique=False, nullable=False, index=True)
    user = db.Column(db.String(20), unique=False, nullable=True, index=True)
