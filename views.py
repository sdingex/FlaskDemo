__author__ = 'Think'
# -*- coding: utf-8 -*-
import exceptions
from flask import render_template, flash, redirect, session, url_for, request
from FlaskDemo import app, db

from models import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adduser/<nickname>/<email>')
def adduser(nickname, email):
    u = User(nickname=nickname, email=email)
    try:
        db.session.add(u)
        db.session.commit()
        return 'add successful'
    except Exception, e:
        print e
        return 'something go wrong'

@app.route('/getuser/<nickname>')
def getuser(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    
    return render_template('user.html', user=user)

@app.route('/userlist')
def userlist():
    users = User.query.all()

    return render_template('userlist.html', users=users)

@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500