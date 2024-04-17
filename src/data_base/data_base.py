import os
import sqlite3

FILE_PATH = os.path.dirname(os.path.realpath(__file__))
DB_NAME = 'pomogator.db'
DB_FILE_PATH = f'{FILE_PATH}\\{DB_NAME}'


class BotDataBase:
    def __init__(self):
        self.conn = sqlite3.connect(DB_FILE_PATH)
        self.cursor = self.conn.cursor()
        print("Connection to database: Successful")

    def user_exist(self, user_id: int) -> bool:
        query = f"SELECT user_id FROM users WHERE user_id = {user_id}"
        result = self.cursor.execute(query)
        return bool(len(result.fetchall()))

    def get_first_name(self, user_id: int) -> str:
        query = f"SELECT first_name FROM users WHERE user_id = {user_id}"
        result = self.cursor.execute(query)
        return result.fetchall()[0][0]

    def add_friends(self, first_user_id: int, second_user_id: int) -> bool:
        query = f"INSERT INTO friends (first_user_id, second_user_id) VALUES ({first_user_id}, '{second_user_id}')"
        self.cursor.execute(query)
        try:
            self.conn.commit()
        except sqlite3.Error:
            return False
        return True

    def all_friends_id(self, user_id: int) -> list:
        query_first = f"SELECT first_user_id as user_id FROM friends WHERE second_user_id == {user_id}"
        query_second = f"SELECT second_user_id as user_id FROM friends WHERE first_user_id == {user_id}"
        first_users_list = self.cursor.execute(query_first).fetchall()
        second_users_list = self.cursor.execute(query_second).fetchall()
        all_friends = first_users_list + second_users_list

        result = []
        for friend in all_friends:
            result.append(friend[0])
        return result

    def is_new_friend(self, user_id: int, friend_id: int) -> bool:
        return not (friend_id in self.all_friends_id(user_id))

    def add_user(self, user_id: int, first_name: str) -> bool:
        query = f"INSERT INTO users (user_id, first_name) VALUES ({user_id}, '{first_name}')"
        self.cursor.execute(query)
        try:
            self.conn.commit()
        except sqlite3.Error:
            return False
        return True

    def update_users(self, user_id: int, selected_id: str) -> bool:
        query = f"UPDATE users SET selected_id = {selected_id} WHERE user_id = {user_id}"
        self.cursor.execute(query)
        try:
            self.conn.commit()
        except sqlite3.Error:
            return False
        return True

    def get_selected_user_id(self, user_id: int) -> int:
        query = f"SELECT * FROM users WHERE user_id = {user_id}"
        user = self.cursor.execute(query).fetchall()
        return user[0][3]

    def add_wish(self, user_id: int, wish: str) -> bool:
        query = f"INSERT INTO wishes (user_id, wish) VALUES ({user_id}, '{wish}')"
        self.cursor.execute(query)
        try:
            self.conn.commit()
        except sqlite3.Error:
            return False
        return True

    def get_wishes(self, user_id: str) -> list:
        query: str = f"SELECT * FROM wishes WHERE user_id = {user_id} GROUP BY wish ORDER BY wish ASC"
        table = self.cursor.execute(query).fetchall()
        result = []
        for wish in table:
            result.append((wish[0], wish[2]))
        return result

    def delete_wish(self, wish_id: int, user_id: int) -> bool:
        print(type(wish_id))
        print(type(user_id))
        wishes = self.get_wishes(str(user_id))
        query = f"DELETE FROM wishes WHERE id = {wishes[wish_id - 1][0]}"
        self.cursor.execute(query)
        try:
            self.conn.commit()
        except sqlite3.Error:
            return False
        return True

    @staticmethod
    def wishes_to_string(wishes: list, header: str) -> str:
        number_of_wishes = 0
        for wish in wishes:
            number_of_wishes += 1
            header += f"{str(number_of_wishes)}: {wish[1]}\n"
        return header
