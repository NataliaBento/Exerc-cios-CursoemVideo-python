import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('MYSQL_URL', 'mysql+mysqlconnector://gr_apps:#granderecife_apps#@localhost/gr_reunioes')
    SQLALCHEMY_TRACK_MODIFICATIONS = False