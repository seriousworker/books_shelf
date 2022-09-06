import sqlite3
from flask import Flask
from flask import render_template
from werkzeug.exceptions import abort


app = Flask(__name__)

def get_connection():
    conn = sqlite3.connect('books_db.sqlite')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/books/list')
def list_books():
    conn = get_connection()
    books = conn.execute('SELECT * FROM books;').fetchall()
    conn.close()

    return render_template('books/list.html', books=books)


@app.route('/books/detail/<int:book_id>')
def detail_book(book_id):
    conn = get_connection()
    book = conn.execute('SELECT * FROM books WHERE id = ?', (book_id,)).fetchone()
    conn.close()
    if book is None:
        abort(404)

    return render_template('books/detail/', book=book)

app.run(port=5020, debug=True)

