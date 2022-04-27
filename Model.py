from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = tuple(db.UniqueConstraint('id', 'username', name='my_2uniq'))

    id = db.Column(db.String(), primary_key=True, unique=True)
    username = db.Column(db.String(), primary_key=True)
    location = db.Column(db.String())
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())
    password = db.Column(db.String())
    email = db.Column(db.String())

    def __init__(self, id, api_key, username, location, firstname, lastname, email, password):
        self.id = id
        self.api_key = api_key
        self.username = username
        self.location = location
        self.first_name = firstname
        self.last_name = lastname
        self.email = email
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)

        def serialize(self):
            return {
                'id' : self.id,
                'api_key' : self.api_key,
                'username' : self.username,
                'location' : self.location,
                'firstname' : self.firstname,
                'lastname' : self.lastname,
                'password' : self.password,
                'email' : self.email
            }
    