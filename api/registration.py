from main import db
from classs import Class
from sqlalchemy.orm import relationship
from sqlalchemy import *

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
    
    def register_class(regCourseID, regClassID, regStudentID, regStatus):
        try:
            registration = Registration.query.filter_by(regCourseID = regCourseID, regClassID =regClassID, regStudentID = regStudentID).first()
            registration.regStatus = regStatus
            db.session.commit()
            return 201, registration.json()
        # don't have existing
        except Exception as e:
            try:
                register = Registration(regStudentID, regCourseID, regClassID, regStatus)
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

    def get_student_accepted_courses(regStudentID):
        output = []
        try:
            classList = db.session.query(Registration.regCourseID, Registration.regClassID).filter(Registration.regStudentID==regStudentID, Registration.regStatus=="accepted").all()
            for classes in classList:
                tempDict = {}
                tempDict['courseID'] = classes[0]
                tempDict['classID'] = classes[1]
                tempDict['courseName'] = ''
                output.append(tempDict)
            return 200, output
        except Exception as e:
            return 400, "no classes found" + str(e)
    
    def get_no_accepted(courseID, classID):
        try:
            count = Registration.query.filter_by(regCourseID = courseID, regClassID = classID, regStatus="accepted").count()
            print("my count " + str(count))
            return 200, count
        except Exception as e:
            return str(e), 0

    def get_student_reg(courseID):
        try:
            registrationn = db.session.query(Registration.regCourseID, Registration.regClassID, Class.clsLimit, Registration.regStudentID).join(Class, and_(Class.classID == Registration.regClassID, Class.clsCourseID == Registration.regCourseID)).filter(Registration.regStatus=="enrolled").filter(courseID==Registration.regCourseID).all()
            real = []
            data = {}
            for each in registrationn:
                data["regCourseID"] = each[0]
                data["regClassID"] = each[1]
                data["studentName"] = ""
                data['clsLimit'] = each[2]
                data['studentID'] = each[3]
                code, data['taken'] = Registration.get_no_accepted(data['regCourseID'], data["regClassID"])
                real.append(data)
                data = {}
            return 200, real
        except Exception as e:
            return 404, "There are no student registrations." + str(e)
    
    def get_enrolled_courseID():
        courses = []
        try:
            for reg in db.session.query(Registration.regCourseID).distinct():
                courseData = {}
                courseData['regCourseID'] = reg[0]
                courseData['courseName'] = ""
                courses.append(courseData)
            return 200, courses
        except Exception as e:
            return 400, "Couldn't get courses. " + str(e)
        
