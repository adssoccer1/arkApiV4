from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate
db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    #Using a production configuration
    #app.config.from_object('config.ProdConfig')
    # Using a development configuration
    app.config.from_object('config.DevConfig')
    db.init_app(app)
    #data.init_app(app)

    CORS(app)

    with app.app_context():
        from . import routes #import routes
        db.create_all()  #create sql tables for our data models.
        print("created all models!", db.metadata.tables.keys())
        #updateData()
        return [app, db]
