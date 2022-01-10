# pythonファイルうがインポートされる時に呼ばれる
from flask import Flask

# Flaskアプリケーションオブジェクト
app = Flask(__name__)

import flaskr.main

from flaskr import db
db.create_books_table()