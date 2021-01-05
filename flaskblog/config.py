import os


class Config():
    SECRET_KEY = 'b92fb348d37c63af5ede57acd67e4ca8'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
