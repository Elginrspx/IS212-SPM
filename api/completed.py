from main import db
from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKeyConstraint


class Completed(db.Model):
    __tablename__ = 'completedCourses'

    ccStudentID = db.Column(db.Integer, db.ForeignKey('students.studentID', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    completedCName = db.Column(db.String(30), primary_key=True)

    # user = relationship('User', backref='child')
    studentCompleted = db.relationship(
    'Student', primaryjoin='Student.studentID == Completed.ccStudentID', backref='completedCourses')

    def __init__(self, ccStudentID, completedCName):
        self.ccStudentID = ccStudentID
        self.completedCName = completedCName
    
    def json(self):
        return {
        "ccStudentID": self.ccStudentID, 
        "completedCName": self.completedCName
        }
    
    def get_completed_by_student(ccStudentID):
        try:
            courseList = Completed.query.filter_by(ccStudentID=ccStudentID).all()
            if len(courseList):
                return 200, [course.json() for course in courseList]
        except Exception as e:
            return 404, "There are no courses found." + str(e)