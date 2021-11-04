from main import db
from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKeyConstraint

class Answer(db.Model):
    __tablename__ = 'answers'

    qnCourseID = db.Column(db.Integer, primary_key=True)
    qnClassID = db.Column(db.String(30), nullable=False)
    qnSectionID = db.Column(db.String(30))
    answers = db.Column(db.String(255))