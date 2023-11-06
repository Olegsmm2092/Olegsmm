from models.model import User, Unit  
from werkzeug.security import generate_password_hash
from extentions import db


def create_tables():
    db.drop_all()
    db.create_all()


def seed_user_db(username, password):
    new_user = User(username=username, password=password) # add True for first user to jwt token
    new_user.password_hash = generate_password_hash(password)
    # Add and commit the new user to the database
    db.session.add(new_user)
    db.session.commit()

    # Create a new unit
    new_unit = Unit(name=new_user.username, desc='role warrior', user_id=new_user.id)
    db.session.add(new_unit)
    db.session.commit()

    print(f"User {username} added successfully!")
    db.session.close()

