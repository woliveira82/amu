import os.path

def sqlite_path():
    sqlite_path = os.path.dirname(os.path.abspath(__file__))
    return sqlite_path

ENV = 'production'
DEBUG = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}storage.db'.format(sqlite_path())
SQLALCHEMY_TRACK_MODIFICATIONS = False