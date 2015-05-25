#!/usr/bin/python
from flup.server.fcgi import WSGIServer
from FlaskDemo import app

if __name__ == '__main__':
    WSGIServer(app, bindAddress='/tmp/flaskr-fcgi.sock').run()