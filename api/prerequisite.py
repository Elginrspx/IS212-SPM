from main import db
from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKeyConstraint


class Prerequisite(db.Model):
    __tablename__ = 'prerequisites'

    prereqCourseID = db.Column(db.String(30), db.ForeignKey('courses.courseID', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    prereqName = db.Column(db.String(30), primary_key=True)

    coursePrereq = db.relationship(
    'Course', primaryjoin='Prerequisite.prereqCourseID == Course.courseID', backref='prerequisites')

    def __init__(self, prereqCourseID, prereqName):
        self.prereqCourseID = prereqCourseID
        self.prereqName = prereqName

    def json(self):
        return {
            "prereqCourseID" : self.prereqCourseID,
            "prereqName" : self.prereqName
        }
    
    def get_prereqs(prereqCourseID):
        try:
            prereqCourseList = Prerequisite.query.filter_by(prereqCourseID = prereqCourseID).all()
            if len(prereqCourseList):
                return 200, [course.json() for course in prereqCourseList]
        except Exception as e:
            return 404, "No courses found. " + str(e)