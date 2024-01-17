from flask import Flask, request, jsonify
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/<name>')
def print_name(name):
    return f'Hello, {name}' 


if __name__ == "__main__":
    app.run(debug=True)