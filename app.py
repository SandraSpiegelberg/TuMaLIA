"""Main application file for the TuMaLIA flask web application a tutoring mate."""
from flask import Flask
import os

from data_models import db
from data_manager import DataManager


app = Flask(__name__)

#set the URI for SQLite database using an absolute path, after initializing Flask app
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, 'data/tumalia.db')}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#output of SQL commands in the console
app.config['SQLALCHEMY_ECHO'] = True

#link SQLAlchemy db object to the Flask app
db.init_app(app)

dm = DataManager()


@app.route('/', methods=['GET'])
def home():
    """Home page of the application."""
    return "Hello, World!"


if __name__ == "__main__":
    #create the database, only run once
    with app.app_context():
        db.drop_all()
        db.create_all()

        #create some test data
        print(dm.create_user(username='testuser', email='testuser@test.de', password_hash='hashedpassword'))
        print(dm.create_thread(user_id=1))
        print(dm.create_message(thread_id=1, content='Hello test_user!', role='assistant'))

        #read some test data
        test_user = dm.get_user(user_id=1)
        print(test_user)
        test_thread = dm.get_thread(thread_id=1)
        print(test_thread)
        test_message = dm.get_message(message_id=1)
        print(test_message)

        #update some test data
        print(dm.update_user(user_id=1, username='updated_testuser'))
        print(dm.update_thread(thread_id=1))
        print(dm.update_message(message_id=1, role='user'))

        #delete some test data
        print(dm.create_user(username='testuser2', email='testuser2@test.de', password_hash='hashedpassword2'))
        print(dm.create_thread(user_id=2))
        print(dm.create_message(thread_id=2, content='Hello test_user2!', role='assistant2'))
        print(dm.list_users())
    
        print(dm.delete_message(message_id=1))
        print(dm.delete_thread(thread_id=1))
        print(dm.delete_user(user_id=1))


    #app.run(host="0.0.0.0", port=5002, debug=True)