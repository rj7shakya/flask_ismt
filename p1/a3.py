#

# router setup
#  / => welcome
#  /about => About page
#  / contact => Contact page
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return 'About page'


if __name__ == '__main__':
    app.run()
