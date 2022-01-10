from flaskr import app
from flask import render_template
import sqlite3

DATABASE = 'database.db'


@app.route('/')
def index():
    connect = sqlite3.connect(DATABASE)
    db_books = connect.execute('SELECT * FROM books').fetchall()
    connect.close()

    books = []
    for row in db_books:
        books.append({
            'title': row[0],
            'price': row[1],
            'arrival_day': row[2]
        })
    return render_template(
        'index.html',
        books=books
    )


@app.route('/form')
def form():
    return render_template('form.html')
