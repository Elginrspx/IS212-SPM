from main import db
from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKeyConstraint


class Class(db.Model):
    __tablename__ = 'classes'

    clsCourseID = db.Column(db.String(30), db.ForeignKey('courses.courseID', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    classID = db.Column(db.Integer, primary_key=True)
    clsTrainer = db.Column(db.String(30), nullable=False)
    clsStartTime = db.Column(db.String(30), nullable = False)
    clsEndTime = db.Column(db.String(30), nullable=False)
    clsLimit = db.Column(db.Integer, nullable=False)
    regPeriod = db.Column(db.String(30), nullable=False)
    # user = relationship('User', backref='child')
    courseClass = db.relationship(
    'Course', primaryjoin='Class.clsCourseID == Course.courseID', backref='classes')

    def __init__(self, clsCourseID, classID, clsTrainer, clsStartTime, clsEndTime, clsLimit, regPeriod):
        self.clsCourseID = clsCourseID
        self.classID = classID
        self.clsTrainer = clsTrainer
        self.clsStartTime = clsStartTime
        self.clsEndTime = clsEndTime
        self.clsLimit = clsLimit
        self.regPeriod = regPeriod
        

    def json(self):
        return {
            "clsCourseID": self.clsCourseID, 
            "classID": self.classID, 
            "clsTrainer": self.clsTrainer, 
            "clsStartTime": self.clsStartTime, 
            "clsEndTime": self.clsEndTime,
            "clsLimit": self.clsLimit,
            "regPeriod": self.regPeriod
        }

    def json_for_trainer(self):
        return {
            "courseID": self.clsCourseID, 
            "classID": self.classID, 
            "courseName": ""
        }
    
    def get_course_classes(courseID):
        try:
            classList = Class.query.filter_by(clsCourseID=courseID).all()
            if classList:
                return 200, [classs.json() for classs in classList]
        except Exception as e:
            return 404, "No classes found" + str(e)

    def get_class_details(courseID, classID):
        try: 
            classes = Class.query.filter_by(clsCourseID=courseID, classID = classID).first()
            if classes:
                return 200, classes.json()
        except Exception as e:
            return 404, "No classes found" + str(e)

    def get_classes_by_trainer(trainer):
        try: 
            classes = Class.query.filter_by(clsTrainer=trainer).all()
            if classes:
                return 200, [classs.json_for_trainer() for classs in classes]
        except Exception as e:
            return 404, "No classes found" + str(e)
    def prepare_class_details_by_course(courseID):
        try:
            classList = db.session.query(Class.clsCourseID, Class.classID, Class.clsTrainer, Class.clsStartTime, Class.clsEndTime, Class.clsLimit, Class.regPeriod).filter(Class.clsCourseID==courseID).all()
            if classList:
                real = []
                data = {}
                for each in classList:
                    print(each[0])
                    data["clsCourseID"] = each[0]
                    data["classID"] = each[1]
                    data["clsTrainer"] = each[2]
                    data["clsStartTime"] = each[3]
                    data["clsEndTime"] = each[4]
                    data["clsLimit"] = each[5]
                    data["regPeriod"] = each[6]
                    data["noAccepted"] = 0
                    real.append(data)
                    data = {}
                return 200, real
        except Exception as e:
            return 400, "Couldn't find classes. " + str(e)

