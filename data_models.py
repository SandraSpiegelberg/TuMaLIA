"""Create tha SQLAlchemy data models for the application."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """Class for objects who represents an user in the database."""
    __tablename__ = 'Users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password_hash = db.Column(db.Text, nullable=True)

    threads = db.relationship('Thread', backref='user', lazy=True, cascade='all, delete-orphan')


    def __init__(self, username, email, password_hash=None, user_id=None):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password_hash = password_hash


    def __repr__(self):
        return f'User(user_id = {self.user_id}, user_name = {self.username}, email = {self.email})'


    def __str__(self):
        return f'User {self.username} with email {self.email} and id {self.user_id}'


class Thread(db.Model):
    """Class for the threads in the database."""
    __tablename__ = 'Threads'

    thread_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_date = db.Column(db.String(20), nullable=False)
    update_date = db.Column(db.String(20), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'), nullable=False)

    messages = db.relationship('Message', backref='thread', lazy=True, cascade='all, delete-orphan')


    def __init__(self, create_date, user_id, update_date=None, thread_id=None):
        self.thread_id = thread_id
        self.create_date = create_date
        self.update_date = update_date
        self.user_id = user_id


    def __repr__(self):
        return f'''Thread(thread_id = {self.thread_id}, create_date = {self.create_date},
            update_date = {self.update_date}, user_id = {self.user_id})'''


    def __str__(self):
        return f'''Thread {self.thread_id} created on {self.create_date} and
            updated on {self.update_date} by user with id {self.user_id}'''


class Message(db.Model):
    """Class for the messages of a thread in the database."""
    __tablename__ = 'Messages'

    message_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    role = db.Column(db.String(20), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    thread_id = db.Column(db.Integer, db.ForeignKey('Threads.thread_id'), nullable=False)


    def __init__(self, content, role, timestamp, thread_id, message_id=None):
        self.message_id = message_id
        self.content = content
        self.role = role
        self.timestamp = timestamp
        self.thread_id = thread_id


    def __repr__(self):
        return f'''Message(message_id = {self.message_id}, content = {self.content},
            role = {self.role}, thread_id = {self.thread_id}, timestamp = {self.timestamp})'''

    def __str__(self):
        return f'''Message {self.message_id} with role {self.role} in thread {self.thread_id} is:
            {self.content} and was creadted on {self.timestamp}'''
