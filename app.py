import os

from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#config
#app.config.from_object(os.environ['APP_SETTINGS'])
app.secret_key = '\xa1\xc74jhw\xce\x88]\xf42`\xdbX\x0c\x1d\x8en_\x8b\x03\xf2GJ'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

# create sqlalchemy object
db = SQLAlchemy(app)

from models import *

def login_required(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if 'logged_in' in session:
            return f(*args,**kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@login_required
def home():
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were just logged in!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('home'))

@app.route('/hostevent', methods=['GET','POST'])
@login_required
def host_event():
    error = None
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template('host.html')

if __name__ == '__main__':
    app.run(DEBUG = True)
