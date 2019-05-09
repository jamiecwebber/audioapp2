# services/sounds/project/api/sounds.py

import os  # new
from flask import Flask, flash, request, redirect, url_for, jsonify, send_from_directory, Blueprint, render_template
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy  # new
from werkzeug.utils import secure_filename
from project import db
from project.api.models import Sound


sounds_blueprint = Blueprint('sounds', __name__, template_folder='./templates')
api = Api(sounds_blueprint)


class SoundsPing(Resource):
    def get(self):
        return {
        'status': 'success',
        'message': 'pong!'
    }

api.add_resource(SoundsPing, '/sounds/ping')

@sounds_blueprint.route('/', methods=['GET'])
def index():
	return render_template('index.html')



@sounds_blueprint.route('/sounds', methods=['GET', 'POST'])
def sounds():
	if request.method == 'POST':
		# check if the post request has the file part
		file = request.files['file']
		title = request.form['title']
		filename = secure_filename(file.filename)
		file_path = os.path.join('./media', filename)
		file.save(file_path)
		db.session.add(Sound(title=title, file_path=file_path))
		db.session.commit()
		return 'success'
	if request.method == 'GET':
		response_object = {
			'status': 'success',
			'data': {
				'sounds': 'list of sounds here'
			}
		}
		return jsonify(response_object), 200


@sounds_blueprint.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)