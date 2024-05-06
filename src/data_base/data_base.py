import os
import sqlite3

FILE_PATH = os.path.dirname(os.path.realpath(__file__))
DB_NAME = 'poly_scheduler.db'
DB_FILE_PATH = f'{FILE_PATH}/{DB_NAME}'


class BotDataBase:
    def __init__(self):
        self.conn = sqlite3.connect(DB_FILE_PATH)
        self.cursor = self.conn.cursor()
        print("Connection to database: Successful")

    def user_exist(self, user_id: int) -> bool:
        query = f"SELECT user_id FROM users WHERE user_id = {user_id}"
        result = self.cursor.execute(query)
        return bool(len(result.fetchall()))

    def add_user(self, user_id: int, group_number: int) -> bool:
        query = f"INSERT INTO users (user_id, group_number) VALUES ({user_id}, '{group_number}')"
        self.cursor.execute(query)
        try:
            self.conn.commit()
        except sqlite3.Error:
            return False
        return True

    def get_group_id(self, user_id: int) -> int:
        query = f"SELECT group_number FROM users WHERE user_id = {user_id}"
        user = self.cursor.execute(query).fetchall()
        return user[0][0]

    def update_group_number(self, user_id: int, new_group_number: int) -> bool:
        query = f"UPDATE users SET group_number = {new_group_number} WHERE user_id = {user_id};"
        self.cursor.execute(query)
        try:
            self.conn.commit()
        except sqlite3.Error:
            return False
        return True

