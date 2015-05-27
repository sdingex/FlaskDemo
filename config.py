__author__ = 'Think'
import os
basedir = os.path.abspath(os.path.dirname(__file__))
"""
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
"""

# SQLALCHEMY_DATABASE_URI = 'mysql://root:luojiancom@localhost/flaskdb'
SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost/flaskdb'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

"""
SQLALCHEMY_DATABASE_URI = 'mysql://kw3:123456@localhost/kw3_article'
SQLALCHEMY_BINDS = {
    'game': 'mysql://kw3:123456@localhost/kw_game',
}
"""