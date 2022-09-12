from application import db
from application.models import Book
from faker import Faker

f = Faker()

for _ in range(25):
    title = f.word().capitalize()
    author = f'{f.last_name()} {f.first_name()}'
    db.session.add(Book(title=title, author=author))
db.session.commit()
