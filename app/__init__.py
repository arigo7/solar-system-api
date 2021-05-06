from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv # this allows us to bring our .env variables from .env
import os # allow us to get those env variables with the method

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None): # this parameter _ how does it know where our test env is?
    app = Flask(__name__)

    if not test_config: #if test_config env is False or None
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False ## why is this set to false?
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI") # this os.environ.get - gets an environment variable ("SQLALCHEMY_DATABASE_URI")
    else: #use Test database if testing env is True
        app.config["TESTING"] = True # turns testing mode on
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI") ## in this case it uses the variable to set our env to the testing db env

    db.init_app(app)
    migrate.init_app(app, db)

    #integrate model
    from app.models.planet import Planet # grabbing my models
    from .routes import planet_bp # where my routes are
    app.register_blueprint(planet_bp) # grabbing blue prints

#grabbing it all from everywhere to be able to run my app
    return app
