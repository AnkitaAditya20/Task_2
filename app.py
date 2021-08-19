from flask import Flask
from flask_restful import Api
from configuration.config import initialize_db
from urls.url import initialize_routes
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost:27017/projecthub'
}

initialize_db(app)
initialize_routes(api)

if __name__ == "__main__":
    app.run(debug=True)