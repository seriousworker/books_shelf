from application import app, db
from application.models import Book


if __name__ == '__main__':
    app.run(debug=True, port=5050)
