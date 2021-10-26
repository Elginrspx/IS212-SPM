from main import db
<<<<<<< Updated upstream
=======
from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKeyConstraint
from classs import Class
>>>>>>> Stashed changes


class Section(db.Model):
    __tablename__ = 'sections'

    secCourseID = db.Column(db.String(30), primary_key=True)
    secClassID = db.Column(db.Integer, nullable=False, primary_key=True)
    sectionID = db.Column(db.String(30), nullable=False, primary_key=True)
    noOfQns = db.Column(db.Integer, nullable=False)
    
    __table_args__ = (ForeignKeyConstraint([secCourseID, secClassID],
                    [Class.clsCourseID, Class.classID]),
                      {})
    classSection = db.relationship(
    'Class', primaryjoin='and_(Class.classID == Section.secClassID, Class.clsCourseID == Section.secCourseID)', backref='sections')

    def __init__(self, secCourseID, secClassID, sectionID, noOfQns):
        self.secCourseID = secCourseID
        self.secClassID = secClassID
        self.sectionID = sectionID
        self.noOfQns = noOfQns


    def json(self):
        return {
            "secCourseID" : self.secCourseID,
            "secClassID": self.secClassID,
            "sectionID" : self.sectionID,
            "noOfQns": self.noOfQns
        }