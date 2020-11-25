from qa327 import app
from flask_sqlalchemy import SQLAlchemy

"""
This file defines all models used by the server
These models provide us a object-oriented access
to the underlying database, so we don't need to 
write SQL queries such as 'select', 'update' etc.
"""


db = SQLAlchemy()
db.init_app(app)


class User(db.Model):
    """
    A user model which defines the sql table
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    balance = db.Column(db.Integer)

class Ticket(db.Model):
    name = db.Column(db.String(1000), primary_key=True)
    seller_id = db.Column(db.Integer,db.ForeignKey(User.id))
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    expires = db.Column(db.Date)

    seller = db.relationship('User',foreign_keys='Ticket.seller_id')

# it creates all the SQL tables if they do not exist
with app.app_context():
    db.create_all()
    db.session.commit()
