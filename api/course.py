from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.orm import relationship
from flask_cors import CORS
from os import environ
import json
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/systemdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Course(db.Model):
    __tablename__ = 'courses'

    courseID = db.Column(db.String(30), primary_key=True)
    courseName = db.Column(db.String(30), nullable = False)
    cDescription = db.Column(db.Text, nullable=False)
    cOutline = db.Column(db.Text, nullable=False)
    have = db.Column(db.Boolean, nullable = False)

    def __init__(self, courseID, courseName, cDescription, cOutline, have):
        self.courseID = courseID
        self.courseName = courseName
        self.cDescription = cDescription
        self.cOutline = cOutline
        self.have = have

    def json(self):
        return {
            "courseID" : self.courseID,
            "courseName" : self.courseName,
            "cDescription" : self.cDescription,
            "cOutline" : self.cOutline,
            "have": self.have
        }

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

# class Registration(db.Model):
#     __tablename__ = 'registrations'

#     regStudentID = db.column(db.Integer, db.ForeignKey('classes.clsCourseID', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
#     clsCourseID = db.Column(db.String(30), db.ForeignKey('classes.clsCourseID', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
#     classID = db.Column(db.Integer,db.ForeignKey('classes.classID', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
#     clsTrainer = db.Column(db.String(30), nullable=False)
#     clsStartTime = db.Column(db.String(30), nullable = False)
#     clsEndTime = db.Column(db.String(30), nullable=False)
#     clsLimit = db.Column(db.Integer, nullable=False)
#     regPeriod = db.Column(db.String(30), nullable=False)
#     # user = relationship('User', backref='child')
#     classRegistration = db.relationship(
#     'Course', primaryjoin='Class.clsCourseID == Course.courseID', backref='classes')

#     def __init__(self, clsCourseID, classID, clsTrainer, clsStartTime, clsEndTime, clsLimit, regPeriod):
#         self.clsCourseID = clsCourseID
#         self.classID = classID
#         self.clsTrainer = clsTrainer
#         self.clsStartTime = clsStartTime
#         self.clsEndTime = clsEndTime
#         self.clsLimit = clsLimit
#         self.regPeriod = regPeriod
        

#     def json(self):
#         return {
#         "clsCourseID": self.clsCourseID, 
#         "classID": self.classID, 
#         "clsTrainer": self.clsTrainer, 
#         "clsStartTime": self.clsStartTime, 
#         "clsEndTime": self.clsEndTime,
#         "clsLimit": self.clsLimit,
#         "regPeriod": self.regPeriod
#         }


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


# class Section(db.Model):
#     __tablename__ = 'sections'

#     secCourseID = db.Column(db.String(30), db.ForeignKey('Class.clsCourseID', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
#     secClassID = db.Column(db.Integer, db.ForeignKey('Class.classID', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
#     sectionID = db.Column(db.String(30), primary_key=True)
    
#     # user = relationship('User', backref='child')
#     classSection1 = db.relationship(
#     'Class', primaryjoin='Class.clsCourseID == Section.secCourseID', backref='sections')
#     classSection2 = db.relationship(
#     'Class', primaryjoin='Class.classID == Section.secClassID', backref='sections')
    
#     def __init__(self, secCourseID, secClassID, sectionID):
#         self.secCourseID = secCourseID
#         self.secClassID = secClassID
#         self.sectionID = sectionID
        

#     def json(self):
#         return {
#         "secCourseID": self.secCourseID, 
#         "secClassID": self.secClassID, 
#         "sectionID": self.sectionID
#         }


# GET all Courses (not finalised, might want to add prereqs to return value and condition to only appear if classes are available, but this works for first sprint...?)
@app.route("/courses")
def get_all_courses():
    try:
        courseList = Course.query.all()
        
        if len(courseList):
            print(courseList)
            print("meep")
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "courses": [course.json() for course in courseList]
                    }
                }
            )
    except Exception as e:
        return jsonify(
            {
                "code": 404,
                "message": "There are no courses." + str(e)
            }
        ), 404

# GET Course Details By courseID !!!! STILL IN PROGRESS LOL
@app.route("/courses/<string:courseID>")
def get_course_details(courseID):
    try: 
        course = Course.query.filter_by(courseID=courseID).first()
        if course:
            return jsonify(
                {
                    "code":200,
                    "data": {
                        "course" : course.json()
                        }
                }
            )
    except Exception as e:
        return jsonify({"message": "Course is not found." + str(e)}), 404

# GET Classes by courseID
@app.route("/classList/<string:courseID>")
def get_course_classes(courseID):
    try:
        classList = Class.query.filter_by(clsCourseID=courseID).all()
        if classList:
            return jsonify(
                {
                    "code":200,
                    "data": {
                        "classes": [classs.json() for classs in classList]
                        }
                }
            )
    except Exception as e:
        return jsonify({"message": "Class is not found." + str(e)}), 404

# GET Class Details by Course-Class (haven't tested)
@app.route("/classes/<string:courseID>/<string:classID>")
def get_class_details(courseID, classID):
    try: 
        classes = Class.query.filter_by(clsCourseID=courseID, classID = classID).first()
        if classes:
            return jsonify(
                {
                    "code":200,
                    "data": {
                        "class" : classes.json()
                        }

                }
            )
    except Exception as e:
        return jsonify({"message": "Class is not found." + str(e)}), 404

# GET all Prerequisites by course
@app.route("/prereqs/<string:prereqCourseID>")
def get_course_prereq(prereqCourseID):
    try:
        prereqCourseList = Prerequisite.query.filter_by(prereqCourseID = prereqCourseID).all()
        if len(prereqCourseList):
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "courses": [course.json() for course in prereqCourseList]
                    }
                }
            )
    except Exception as e:
        return jsonify(
            {
                "code": 404,
                "message": "There are no courses." + str(e)
            }
        ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2222, debug=True)