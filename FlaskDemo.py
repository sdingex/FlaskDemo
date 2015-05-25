# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from views import *
from views_st import *
import models

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=8888)
