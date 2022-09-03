from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'


app.run(port=5020, debug=True)

