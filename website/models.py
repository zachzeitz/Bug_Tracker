from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class Ticket(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(150))
    data= db.Column(db.String(10000))
    date= db.Column(db.DateTime(timezone=True), default= func.now())
    #sets foreign key to user id, to  differentiate posts between users
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String(150), unique=True)
    password= db.Column(db.String(150))
    first_name= db.Column(db.String(150))
    #allows users to access all tickets they have created
    tickets= db.relationship('Ticket')
