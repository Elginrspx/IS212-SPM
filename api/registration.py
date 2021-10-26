from main import db
from classs import Class
from sqlalchemy import ForeignKeyConstraint

class Registration(db.Model):

    __tablename__ = 'registrations'

    regStudentID = db.Column(db.Integer, primary_key=True)
<<<<<<< Updated upstream
    # regCourseID = db.Column(db.String(30), db.ForeignKey('classes.clsCourseID', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    # regClassID = db.Column(db.Integer,db.ForeignKey('classes.classID', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    regCourseID = db.Column(db.String(30),nullable=False, primary_key = True)
    regClassID = db.Column(db.Integer,nullable=False, primary_key = True)
=======
    regCourseID = db.Column(db.String(30), nullable=False, primary_key = True)
    regClassID = db.Column(db.Integer, nullable=False, primary_key = True)
>>>>>>> Stashed changes
    regStatus = db.Column(db.String(30), nullable=False)
    # user = relationship('User', backref='child')
    __table_args__ = (ForeignKeyConstraint([regCourseID, regClassID],
                                           [Class.clsCourseID, Class.classID]),
                      {})
    classRegistration = db.relationship(
    'Class', primaryjoin='and_(Class.classID == Registration.regClassID, Class.clsCourseID == Registration.regCourseID)', backref='registrations')
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