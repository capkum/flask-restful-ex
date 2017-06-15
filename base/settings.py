SQLALCHEMY_DATABASE_URI = 'mysql://flask:flask123@localhost/flask?charset=utf8'  # noqa
SQLALCHEMY_TRACK_MODIFICATIONS = False

try:
    from base.local_settings import *  # noqa
except ImportError:
    pass
