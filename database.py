import sqlite3


class BaseDiscord(object):
    def __init__(self):
        self.conn = sqlite3.connect('dbUsers.db')
        self.curr = self.conn.cursor()
        self.base_migrate()

    def base_migrate(self):
        self.curr.execute('create table if not exists users(id, user, rating, last_match_id)')
        return 'Миграции в бд проведены!'

    def update_user(self, user, rating, last_match_id):
        self.curr.execute(f'UPDATE users SET rating = {rating}, last_match_id = {last_match_id} WHERE user = {user}')
        self.conn.commit()
        return 'Изменения успешно внесены!'

    def add_user(self, id, user, rating, last_match_id):
        self.curr.execute(f'insert into users (id, user, rating, last_match_id) VALUES ({id}, {user}, {rating}, {last_match_id})')
        self.conn.commit()
        return 'Пошльзователь внесен в БД!'

    def get_users(self):
        self.curr.execute(f'select id from users')
        return [i[0] for i in self.curr.fetchall()]



print(BaseDiscord().get_users())
