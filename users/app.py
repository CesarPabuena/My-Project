from flask import Flask, jsonify, request
from utils.constants import(Settings)
from flask_migrate import Migrate
from database.db_sqlalchemy import db
from database.db_connection import Connection
import models
from api_routes import register_routes


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = Connection.URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Connection.ACTIVE_MODIFICATE

db.init_app(app)
migrate = Migrate(app, db)

register_routes(app)

@app.route ('/')
def index():
    return jsonify({"data":"Hello World!"})

if __name__ == "__main__":
    app.run(host = Settings.HOST, port = Settings.PORT, debug = Settings.DEBUG)
    