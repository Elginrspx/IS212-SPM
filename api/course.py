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

    def __init__(self, courseID, cDescription, cOutline, cBadge):
        self.courseID = courseID
        self.courseName = courseName
        self.cDescription = cDescription
        self.cOutline = cOutline

    def json(self):
        return {
            "courseID" : self.courseID,
            "courseName" : self.courseName,
            "cDescription" : self.cDescription,
            "cOutline" : self.cOutline
        }

class Class(db.Model):
    __tablename__ = 'classes'

    clsCourseID = db.Column(db.String(30), db.ForeignKey('courses.courseID', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    classID = db.Column(db.Integer, primary_key=True)
    clsTrainer = db.Column(db.String(30), nullable=False)
    clsStartTime = db.Column(db.String(30), nullable = False)
    clsEndTime = db.Column(db.String(30), nullable=False)
    # user = relationship('User', backref='child')
    courseClass = db.relationship(
    'Course', primaryjoin='Class.clsCourseID == Course.courseID', backref='classes')

    def __init__(self, clsCourseID, classID, clsTrainer, clsStartTime, clsEndTime):
        self.clsCourseID = clsCourseID
        self.classID = classID
        self.clsTrainer = clsTrainer
        self.clsStartTime = clsStartTime
        self.clsEndTime = clsEndTime
        

    def json(self):
        return {
        "clsCourseID": self.clsCourseID, 
        "classID": self.classID, 
        "clsTrainer": self.clsTrainer, 
        "clsStartTime": self.clsStartTime, 
        "clsEndTime": self.clsEndTime
        }

class Prerequisite(db.Model):
    __tablename__ = 'prerequisites'

    reqCourseID = db.Column(db.String(30), db.ForeignKey('courses.courseID', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    reqBadgeID = db.Column(db.String(30), primary_key=True)

    coursePrereq = db.relationship(
    'Course', primaryjoin='Prerequisite.reqCourseID == Course.courseID', backref='prerequisites')

    def __init__(self, reqCourseID, reqBadgeID):
        self.reqCourseID = reqCourseID
        self.reqBadgeID = reqBadgeID

    def json(self):
        return {
            "reqCourseID" : self.reqCourseID,
            "reqBadgeID" : self.reqBadgeID
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
            print("yay")
            try:
                classList = Class.query.filter_by(clsCourseID=courseID).first()
            except Exception as e:
                print("oh no")
                return jsonify({
                    "code": 404,
                    "data": {
                        "course" : course.json(),
                        "classes" : "No classes for this course yet"
                        },
                    })
            return jsonify(
                {
                    "code":200,
                    "data": {
                        "course" : course.json(),
                        "classes" : [classes.json() for classes in classList]
                        }

                }
            )
    except Exception as e:
        return jsonify({"message": "Course is not found." + str(e)}), 404

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
@app.route("/courses/<string:courseID>")
def get_course_prereq():
    try:
        courseList = Course.query.all()
        if len(courseList):
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2222, debug=True)