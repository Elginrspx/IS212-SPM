from main import db
from classs import Class
from sqlalchemy import ForeignKeyConstraint

class Registration(db.Model):

    __tablename__ = 'registrations'

    regStudentID = db.Column(db.Integer, primary_key=True)
    regCourseID = db.Column(db.String(30), nullable=False, primary_key = True)
    regClassID = db.Column(db.Integer, nullable=False, primary_key = True)
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
    
    def register_cLass(regCourseID, regClassID, regStudentID, regStatus):
        try:
            registration = Registration.query.filter_by(regCourseID = regCourseID, regClassID =regClassID, regStudentID = regStudentID).first()
            registration.regStatus = regStatus
            db.session.commit()
            return 201, registration.json()
        # don't have existing
        except Exception as e:
            try:
                register = Registration(regCourseID, regClassID, regStudentID, regStatus)
                db.session.add(register)
                db.session.commit()
                return 201, register.json()
            except Exception as e:
                return 500, "Could not update registration. " + str(e)






    def assign_registration(regCourseID, regClassID, regStudentID):
        registration = Registration.query.filter_by(regCourseID = regCourseID, regClassID =regClassID, regStudentID = regStudentID).first()
        registration.regStatus = "accepted"
        db.session.commit()
        return 201, registration.json()