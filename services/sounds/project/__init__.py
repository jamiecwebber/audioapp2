# services/users/project/__init__.py


import os  # new
from flask import Flask, flash, request, redirect, url_for, jsonify, send_from_directory
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy  # new
from werkzeug.utils imort secure_filename

UPLOAD_FOLDER = './media'

# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')  # new
app.config.from_object(app_settings)      # new
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

# instantiate the db
db = SQLAlchemy(app)  # new


# model
class Sound(db.Model):  # new
    __tablename__ = 'sounds'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    file_path = db.Column(db.String(128), nullable=False)
    def __init__(self, username, file_path):
        self.username = username
        self.file_path = file_path


class SoundsPing(Resource):
    def get(self):
        return {
        'status': 'success',
        'message': 'pong!'
    }

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
			filename = secure_filename(file.filename):
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(url_for('uploaded_file', filename=filename))


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


api.add_resource(SoundsPing, '/users/ping')