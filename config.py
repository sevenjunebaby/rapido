import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "rapido.db")}'
SQLALCHEMY_TRACK_MODIFICATIONS = False