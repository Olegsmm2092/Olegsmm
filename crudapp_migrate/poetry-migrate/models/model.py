from datetime import datetime
from extentions import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def as_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'password_hash': self.password_hash,
        }
    

class Unit(db.Model):
    __tablename__ = 'units'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)
    desc = db.Column(db.String, nullable=False)
    photo = db.Column(db.LargeBinary, default=b'\x00\x01\x02\x03')


    def as_dict(self):
        return {
            'unitid': self.id,
            'name': self.name,
            'desc': self.desc,
        }