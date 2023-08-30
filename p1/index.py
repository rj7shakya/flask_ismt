from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/home')
def home():
    return 'HOME PAGE'


if __name__ == '__main__':
    app.run()
