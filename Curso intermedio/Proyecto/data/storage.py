import sqlite3
from model.user import User

class UserStorage:
    def __init__(self, db_path='users.db'):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    dni TEXT NOT NULL,
                    email TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    photo TEXT
                )
            ''')

    def create_user(self, name, dni, email, phone, photo=None):
        with self.conn:
            cursor = self.conn.execute('''
                INSERT INTO users (name, dni, email, phone, photo)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, dni, email, phone, photo))
            user_id = cursor.lastrowid
            return User(user_id, name, dni, email, phone, photo)

    def get_all_users(self):
        cursor = self.conn.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        return [User(row['id'], row['name'], row['dni'], row['email'], row['phone'], row['photo']) for row in rows]

    def update_user(self, user_id, name, dni, email, phone, photo=None):
        with self.conn:
            self.conn.execute('''
                UPDATE users
                SET name = ?, dni = ?, email = ?, phone = ?, photo = ?
                WHERE id = ?
            ''', (name, dni, email, phone, photo, user_id))
            return self.get_user_by_id(user_id)

    def get_user_by_id(self, user_id):
        cursor = self.conn.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        row = cursor.fetchone()
        if row:
            return User(row['id'], row['name'], row['dni'], row['email'], row['phone'], row['photo'])
        return None

    def delete_user(self, user_id):
        with self.conn:
            cursor = self.conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
            return cursor.rowcount > 0