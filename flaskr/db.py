import sqlite3

DATABASE = 'database.db'


def create_books_table():
    # コネクションオブジェクト（データベースへのアクセス）
    connect = sqlite3.connect(DATABASE)
    connect.execute('CREATE TABLE IF NOT EXISTS books (title, price, arrival_day)')
    connect.close()
