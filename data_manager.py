"""Module to manage data operations for Users, Threads and their Messages."""
from datetime import datetime
from data_models import User, Thread, Message, db

class DataManager:
    """Class to manage CRUD operations for Users, Threads and Messages."""
    def create_user(self, username, email, password_hash=None):
        """Creates a new user in the database."""
        new_user = User(username=username, email=email, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()
        return {'success': True,
                'message': f'User {username} successfully added.',
                'user': new_user}


    def create_thread(self, user_id):
        """Creates a new thread for a given user."""
        date_now = datetime.now().isoformat(sep=' ', timespec='seconds')
        new_thread = Thread(user_id=user_id, create_date=date_now, update_date=None)
        db.session.add(new_thread)
        db.session.commit()
        return {'success': True,
                'message': f'Thread {new_thread.thread_id} successfully added.',
                'thread': new_thread}


    def create_message(self, thread_id, content, role):
        """Creates a new message in a given thread."""
        date_now = datetime.now()
        new_message = Message(thread_id=thread_id, content=content, role=role, timestamp=date_now)
        db.session.add(new_message)
        db.session.commit()
        return {'success': True,
                'message': f'Message {new_message.message_id} successfully added.',
                'thread_message': new_message}


    def get_user(self, user_id):
        """Gets a user by their ID."""
        user = db.session.get(User, user_id)
        return user


    def get_thread(self, thread_id):
        """Gets a thread by its ID."""
        thread = db.session.get(Thread, thread_id)
        return thread


    def get_message(self, message_id):
        """Gets a message by its ID."""
        message = db.session.get(Message, message_id)
        return message


    def get_threads_by_user(self, user_id):
        """Gets all threads for a given user."""
        user = db.session.get(User, user_id)
        if not user:
            return {'success': False,
                    'message': f'No user with id {user_id} found.'}
        return user.threads


    def get_messages_by_thread(self, thread_id):
        """Gets all messages for a given thread."""
        thread = db.session.get(Thread, thread_id)
        if not thread:
            return {'success': False,
                    'message': f'No thread with id {thread_id} found.'}
        return thread.messages


    def list_users(self):
        """Lists all user in the database."""
        users = User.query.all()
        return users


    def update_user(self, user_id, username=None, email=None, password_hash=None):
        """Updates user information (name, email or password)."""
        user = self.get_user(user_id)
        if not user:
            return {'success': False,
                    'message': f'User with id {user_id} does not exist.'}
        if username:
            user.username = username
        if email:
            user.email = email
        if password_hash:
            user.password_hash = password_hash
        db.session.commit()
        return {'success': True,
                'message': f'User {user.username} successfully updated.',
                'user': user}


    def update_thread(self, thread_id):
        """Updates the update_date of a thread to the current time."""
        thread = self.get_thread(thread_id)
        if not thread:
            return {'success': False,
                    'message': f'Thread with id {thread_id} does not exist.'}
        date_now = datetime.now().isoformat(sep=' ', timespec='seconds')
        thread.update_date = date_now
        db.session.commit()
        return {'success': True,
                'message': f'Thread {thread_id} successfully updated.',
                'thread': thread}


    def update_message(self, message_id, content=None, role=None):
        """Updates message content or role."""
        message = self.get_message(message_id)
        if not message:
            return {'success': False,
                    'message': f'Message with id {message_id} does not exist.'}
        if content:
            message.content = content
        if role:
            message.role = role
        db.session.commit()
        return {'success': True,
                'message': f'Message {message_id} successfully updated.',
                'thread_message': message}


    def delete_user(self, user_id):
        """Deletes a user and all their threads and messages."""
        user =  self.get_user(user_id)
        if not user:
            return {'success': False,
                    'message': f'User with id {user_id} does not exist.'}
        name = user.username
        db.session.delete(user)
        db.session.commit()
        return {'success': True,
                'message': f'User {name} with id {user_id} has been deleted.',
                'user': user}


    def delete_thread(self, thread_id):
        """Deletes a thread and all its messages."""
        thread = self.get_thread(thread_id)
        if not thread:
            return {'success': False,
                    'message': f'Thread with id {thread_id} does not exist.'}
        db.session.delete(thread)
        db.session.commit()
        return {'success': True,
                'message': f'Thread with id {thread_id} has been deleted.',
                'thread': thread}


    def delete_message(self, message_id):
        """Deletes a message."""
        message = self.get_message(message_id)
        if not message:
            return {'success': False,
                    'message': f'Message with id {message_id} does not exist.'}
        db.session.delete(message)
        db.session.commit()
        return {'success': True,
                'message': f'Message with id {message_id} has been deleted.',
                'thread_message': message}
