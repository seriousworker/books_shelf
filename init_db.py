import sqlite3
from faker import Faker

connection = sqlite3.connect('books_db.sqlite')

with open('schema.sql') as f:
    connection.executescript(f.read())


cursor = connection.cursor()
f = Faker()

for _ in range(25):
    title = f.word().capitalize()
    author = f'{f.last_name()} {f.first_name()}'
    cursor.execute('INSERT INTO books(title, author) VALUES (?, ?)', (title, author))

connection.commit()
connection.close()
