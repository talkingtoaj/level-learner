import sqlite3
from models import User
import threading

class Database:
    _local = threading.local()

    def __init__(self, db_name='users.db'):
        self.db_name = db_name
        self.create_table()

    def get_connection(self):
        if not hasattr(self._local, 'connection'):
            self._local.connection = sqlite3.connect(self.db_name)
        return self._local.connection

    def create_table(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                current_level INTEGER,
                quiz_scores TEXT
            )
        ''')
        conn.commit()

    def get_user(self, username):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user_data = cursor.fetchone()
        if user_data:
            return User(username=user_data[0], current_level=user_data[1], quiz_scores=eval(user_data[2]))
        return None

    def create_user(self, username):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, current_level, quiz_scores) VALUES (?, ?, ?)',
                       (username, 1, '[]'))
        conn.commit()
        return User(username=username, current_level=1, quiz_scores=[])

    def update_user(self, user):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE users SET current_level = ?, quiz_scores = ? WHERE username = ?',
                       (user.current_level, str(user.quiz_scores), user.username))
        conn.commit()