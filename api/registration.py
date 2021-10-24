from main import db
from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKeyConstraint
from classs import Class


class Registration(db.Model):

    __tablename__ = 'registrations'

    regStudentID = db.Column(db.Integer, primary_key=True)
    regCourseID = db.Column(db.String(30),nullable=False, primary_key = True)
    regClassID = db.Column(db.Integer,nullable=False, primary_key = True)
    regStatus = db.Column(db.String(30), nullable=False)
    # user = relationship('User', backref='child')
    __table_args__ = (ForeignKeyConstraint([regCourseID, regClassID],
                    [Class.clsCourseID, Class.classID]),
                      {})
    # classRegistration = db.relationship(
    # 'Class', primaryjoin='and_(Class.classID == Registration.regClassID, Class.clsCourseID == Registration.regCourseID)', backref='registrations')
    def __init__(self, regStudentID, regCourseID, regClassID, regStatus):
        self.regStudentID = regStudentID
        self.regCourseID = regCourseID
        self.regClassID = regClassID
        self.regStatus = regStatus
        

    def json(self):
        return {
        "regStudentID": self.regStudentID, 
        "regCourseID": self.regCourseID, 
        "regClassID": self.regClassID, 
        "regStatus": self.regStatus
        }

    #for both student self-enrol and force assignment
    def register_class(regCourseID, regClassID, regStudentID, regStatus):
        if (Registration.query.filter_by(regCourseID=regCourseID, regClassID = regClassID, regStudentID = regStudentID).all()):
            return 400, "The student has already made a registration for this class"
        registration = Registration(regStudentID, regCourseID, regClassID, regStatus)
        try:
            db.session.add(registration)
            db.session.commit()
        except Exception as e:
            return 500, "An error occurred registering to the class. " + str(e)
        return 201, registration.json()

    def assign_registration(regCourseID, regClassID, regStudentID, regStatus):
        try:
            registration = Registration.query.filter_by(regCourseID = regCourseID, regClassID = regClassID, regStudentID = regStudentID).first()
            registration.regStatus = regStatus
            db.session.commit()
        except Exception as e:
            return 500, "Couldn't update the registration. " + str(e)
        return 200, registration.json()