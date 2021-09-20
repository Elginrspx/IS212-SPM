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

class Student(db.Model):
    __tablename__ = 'students'

    studentID = db.Column(db.Integer, primary_key=True)
    studentName = db.Column(db.String(30), nullable=False)
    sPosition = db.Column(db.String(30), nullable = False)


    def __init__(self, studentID, studentName, sPosition):
        self.studentID = studentID
        self.studentName = studentName
        self.sPosition = sPosition


    def json(self):
        return {
            "studentID" : self.studentID,
            "studentName": self.studentName,
            "sPosition" : self.sPosition,
        }

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

# GET all completed Courses by studentID 
@app.route("/completed/<string:ccStudentID>")
def get_students_completed_courses(ccStudentID):
    print(ccStudentID)
    try:
        courseList = Completed.query.filter_by(ccStudentID=ccStudentID).all()
        
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

# GET student info by studentName
@app.route("/student/<string:studentID>")
def get_student(studentID):
    print(studentID)
    try:
        student = Student.query.filter_by(studentID=studentID).first()
        
        if (student):
            print(student)
            print("meep")
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "courses": student.json()
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
    app.run(host='0.0.0.0', port=3333, debug=True)