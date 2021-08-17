from flask_mongoengine import MongoEngine
from flask_mail import Mail
from flask import Flask

app = Flask(__name__)
mail = Mail(app)
db = MongoEngine()


def initialize_mail(app):
    mail.init_app(app)


def initialize_db(app):
    db.init_app(app)