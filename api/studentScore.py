from main import db
from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKeyConstraint


class Score(db.Model):
    __tablename__ = 'scores'

    secStudentID = db.Column(db.Integer, primary_key=True)
    secCourseID = db.Column(db.Integer, primary_key=True)
    secClassID = db.Column(db.String(30), nullable=False)
    sectionID = db.Column(db.String(30))
    scorePercentage = db.Column(db.Integer)


    def __init__(self, secCourseID, secClassID, sectionID, scorePercentage):
        self.secCourseID = secCourseID
        self.secClassID = secClassID
        self.sectionID = sectionID
        self.scorePercentage = scorePercentage


    def json(self):
        return {
            "secCourseID" : self.secCourseID,
            "secClassID": self.secClassID,
            "sectionID" : self.sectionID,
            "scorePercentage": self.scorePercentage
        }
