# services/sounds/project/__init__.py


import os  # new
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy  # new
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './media'


# instantiate the db
db = SQLAlchemy()


# new
def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)
    app.secret_key = "super secret key"

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

    # set up extensions
    db.init_app(app)

    # register blueprints
    from project.api.sounds import sounds_blueprint
    app.register_blueprint(sounds_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}





    return app

