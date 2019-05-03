# services/sounds/project/__init__.py


import os  # new
from flask import Flask, flash, request, redirect, url_for, jsonify, send_from_directory
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



    @app.route('/', methods=['GET', 'POST'])
    def upload_file():
    	if request.method == 'POST':
    		# check if the post request has the file part
    		if 'file' not in request.files:
    			flash('No selected file')
    			return redirect(request.url)
    		file = request.files['file']
    		if file.filename == '':
    			flash("No selected file")
    			return redirect(request.url)
    		if file:
    			filename = secure_filename(file.filename)
    			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    			return redirect(url_for('uploaded_file', filename=filename))


    @app.route('/uploads/<filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'],
                                   filename)

    
    return app

