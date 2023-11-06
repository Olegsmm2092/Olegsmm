from datetime import datetime
from extentions import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    units = db.relationship('Unit', backref='user', passive_deletes=True)

    def as_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'password_hash': self.password_hash,
            'units': [n.as_dict() for n in self.units]
        }
    

class Unit(db.Model):
    __tablename__ = 'units'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)
    desc = db.Column(db.String, nullable=False)
    photo = db.Column(db.LargeBinary, default=b'\x00\x01\x02\x03')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)


    def as_dict(self):
        return {
            'unitid': self.id,
            'name': self.name,
            'desc': self.desc,
            'user_id': self.user_id
        }