# services/sounds/project/api/sounds.py


from flask import Blueprint
from flask_restful import Resource, Api


sounds_blueprint = Blueprint('sounds', __name__)
api = Api(sounds_blueprint)


class SoundsPing(Resource):
    def get(self):
        return {
        'status': 'success',
        'message': 'pong!'
    }



api.add_resource(SoundsPing, '/sounds/ping')