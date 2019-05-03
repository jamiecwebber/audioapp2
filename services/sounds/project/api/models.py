# services/sounds/project/api/models.py


from sqlalchemy.sql import func

from project import db


class Sound(db.Model):

    __tablename__ = 'sounds'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    file_path = db.Column(db.String(128), nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, title, file_path):
        self.title = title
        self.file_path = file_path