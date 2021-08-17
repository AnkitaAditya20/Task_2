from flask import Flask
from flask_restful import Api
from configuration.config import initialize_db, initialize_mail
from urls.url import initialize_routes
from flask_bcrypt import Bcrypt
from urls.errors import *
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'de3b6c8ba4174f'
app.config['MAIL_PASSWORD'] = '72bcf482843e16'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['DEBUG'] = True
mail = Mail(app)

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost:27017/projecthub'
}

initialize_mail(app)
initialize_db(app)
initialize_routes(api)

if __name__ == "__main__":
    app.run(debug=True)