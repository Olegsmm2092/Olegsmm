from flask import Flask, jsonify
import os
from extentions import db

# add migrations
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object('config')
app.config['SECRET_KEY'] = os.urandom(24)
db.init_app(app)

# Import your models (User and Unit) here below the import of db
from models.model import User, Unit

migrate = Migrate(app, db)

@app.route('/')
def flat():
   return '<h3>Crudapp Migrate</h3>'



if __name__ == '__main__':
    from seed_rel import create_tables, seed_user_db
    ...
    # with app.app_context():
        # seed_user_db('unit', '123')
        # seed_user_db('enemy', '123'[::-1])
        # user = User.query.filter_by(username='unit2')
        # users_data = [n.as_dict() for n in user[0]['units']]
        # print(users_data)
        

    # app.run()