from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import DataRequired


app = Flask(__name__)

# Create a Form Class


@app.route('/')

#def index():
#    return "<h1>Hello World! - Wassup</h1>"

def index():
    first_name = 'John'
    return render_template('index.html')

@app.route('/user/<name>')

def user(name):
    return render_template('user.html', user_name = name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template ("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template ("500.html"), 500

