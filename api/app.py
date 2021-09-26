from types import ClassMethodDescriptorType
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import *
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

class Registration(db.Model):
    __tablename__ = 'registrations'

    regStudentID = db.Column(db.Integer, db.ForeignKey('students.studentID', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    regCourseID = db.Column(db.String(30), db.ForeignKey('classes.clsCourseID', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    regClassID = db.Column(db.Integer,db.ForeignKey('classes.classID', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    regStatus = db.Column(db.String(30), nullable=False)
    # user = relationship('User', backref='child')
    classRegistration1 = db.relationship(
    'Class', primaryjoin='Class.clsCourseID == Registration.regCourseID', backref='registrations1')
    classRegistration2 = db.relationship(
    'Class', primaryjoin='Class.classID == Registration.regClassID', backref='registrations2')
    studentRegistration = db.relationship(
    'Student', primaryjoin='Student.studentID == Registration.regStudentID', backref='registrations3')

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

# GET Class Details by Course-Class 
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

# GET all students
@app.route("/students")
def get_all_students():
    try:
        studentList = Student.query.all()
        
        if len(studentList):
            print(studentList)
            print("meep")
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "students": [student.json() for student in studentList]
                    }
                }
            )
    except Exception as e:
        return jsonify(
            {
                "code": 404,
                "message": "There are no students." + str(e)
            }
        ), 404

# GET student info by studentID
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
                        "student": student.json()
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

# GET all student registrations
@app.route("/registration")
def get_all_registration():
    try:
        registrationn = Registration.query.filter_by(regStatus="enrolled").all()
        if (registrationn):
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "registrations": [registration.json() for registration in registrationn]
                    }
                }
            )
    except Exception as e:
        return jsonify(
            {
                "code": 404,
                "message": "There are no student registrations." + str(e)
            }
        ), 404

# GET no of student accepted to class
@app.route("/noAccepted/<string:courseID>/<string:classID>")
def get_no_accepted(courseID, classID):
    try:
        accepted = Registration.query.filter_by(regCourseID = courseID, regClassID = classID, regStatus="accepted").count()
        if (accepted):
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "registrations": accepted
                    }
                }
            )
    except Exception as e:
        return jsonify(
            {
                "code": 404,
                "message": "There are no student registrations." + str(e)
            }
        ), 404

# GET student registrations by course
@app.route("/registration/<string:courseID>")
def get_student_registration(courseID):
    try:
        registrationn = db.session.query(Registration.regCourseID, Registration.regClassID, Student.studentName, Class.clsLimit, Student.studentID).join(Class, and_(Class.classID == Registration.regClassID, Class.clsCourseID == Registration.regCourseID)).join(Student, Student.studentID == Registration.regStudentID).filter(Registration.regStatus=="enrolled").filter(courseID==Registration.regCourseID).all()
        if (registrationn):
            real = []
            data = {}
            for each in registrationn:
                data["regCourseID"] = each[0]
                data["regClassID"] = each[1]
                data["studentName"] = each[2]
                data['clsLimit'] = each[3]
                data['studentID'] = each[4]
                data['taken'] = Registration.query.filter_by(regCourseID = each[0], regClassID = each[1], regStatus="accepted").count()
                real.append(data)
                data = {}
            print(real)
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "registrations": real
                    }
                }
            )
    except Exception as e:
        return jsonify(
            {
                "code": 404,
                "message": "There are no student registrations." + str(e)
            }
        ), 404

# POST registration for courseClass
@app.route("/registerClass", methods=['POST'])
def register_class():
    data = request.get_json()
    print(data['regCourseID'])
    regCourseID = data['regCourseID']
    regClassID = data['regClassID']
    regStudentID = data['regStudentID']
    if (Registration.query.filter_by(regCourseID=regCourseID, regClassID = regClassID, regStudentID = regStudentID).all()):
        return jsonify({"code": 400,"message": "The student has already made a registration for this class"}), 400
 
    
    registration = Registration(**data)
 
    try:
        db.session.add(registration)
        db.session.commit()
    except Exception as e:
        return jsonify({"code": 500, "message": "An error occurred creating the assignment." + str(e)}), 500
 
    return jsonify({"code": 201, "data": registration.json()}), 201


#GET list of course ID & name of those with enrolled students
@app.route("/registrationCourses", methods=["GET"])
def all_reg():
    try:
        # test = db.session.query(func.count('*').group_by(Registration.regCourseID, Registration.regClassID), Registration.regCourseID, Registration.regClassID, Student.studentName).join(Class, and_(Class.classID == Registration.regClassID, Class.clsCourseID == Registration.regCourseID)).join(Student, Student.studentID == Registration.regStudentID).all()
        registration_info = db.session.query(Registration.regCourseID, Registration.regClassID).filter(Registration.regStatus=="enrolled").all()
        # print(test)

        # ape ini idgi 
        if registration_info:
            courseList = []
            courses = []
            # print(registration_info)
            for each in registration_info:
                # print(each[0])
                # print(db.session.query(Course.courseName).filter(Course.courseID == each[0]).first()[0])

                courseName = db.session.query(Course.courseName).filter(Course.courseID == each[0]).first()[0]

                if courseName not in courses:
                    print("lol")
                    # courseList[each[0]] = data["courseName"]
                    courseData = {}
                    courseData["courseName"] = courseName
                    courseData["regCourseID"] = each[0]
                    courseList.append(courseData)
                    courses.append(courseName)
                    print(courseList)
                    # data['assignments']= each.json()
                    # print(data)
            # return jsonify({"assignments": data})
            return jsonify({"code": 200, "courseList": courseList}),200
            # return jsonify({"assignments": [assignment.json() for assignment in test[0]]})
    except Exception as e:
        return jsonify({"message": "Assignment had a problem fetching" + str(e)}), 500


# GET all registrations with class and student table joined
@app.route("/classInfo/<string:courseID>", methods=["GET"])
def all_class_info(courseID):
    try:
        # test = db.session.query(func.count('*').group_by(Registration.regCourseID, Registration.regClassID), Registration.regCourseID, Registration.regClassID, Student.studentName).join(Class, and_(Class.classID == Registration.regClassID, Class.clsCourseID == Registration.regCourseID)).join(Student, Student.studentID == Registration.regStudentID).all()
        classList = db.session.query(Class.clsCourseID, Class.classID, Class.clsTrainer, Class.clsStartTime, Class.clsEndTime, Class.clsLimit, Class.regPeriod).filter(Class.clsCourseID==courseID).all()
        Class.query.filter_by(clsCourseID=courseID).all()        # print(test)

        # ape ini idgi 
        if classList:
            real = []
            data = {}
            print(classList)
            for each in classList:
                print(each[0])
                # print(db.session.query(Course.courseName).filter(Course.courseID == each[0]).first()[0])
                data["clsCourseID"] = each[0]
                data["classID"] = each[1]
                data["clsTrainer"] = each[2]
                data["clsStartTime"] = each[3]
                data["clsEndTime"] = each[4]
                data["clsLimit"] = each[5]
                data["regPeriod"] = each[6]
                data["noAccepted"] = Registration.query.filter_by(regCourseID = each[0], regClassID = each[1], regStatus="accepted").count()
                # data['assignments']= each.json()
                # print(data)
                real.append(data)
                data = {}
            # return jsonify({"assignments": data})
            return jsonify({"code": 200, "classInfo": real}),200
            # return jsonify({"assignments": [assignment.json() for assignment in test[0]]})
    except Exception as e:
        return jsonify({"message": "Assignment had a problem fetching" + str(e)}), 500


# UPDATE registration to accepted
@app.route("/assignRegistration", methods=['PUT'])
def assign_registration():
    try:
        
        print("check")
        data = request.get_json()
        registration = Registration.query.filter_by(regCourseID = data['courseID'], regClassID = data['classID'], regStudentID = data['studentID']).first()
        if data['regStatus'] == "accepted":
            print(registration)
            registration.regStatus = data['regStatus']
            db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": registration.json()
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while updating the user. " + str(e)
            }
        ), 500

# POST registration for courseClass
@app.route("/assignStudent", methods=['POST'])
def force_assign():
    data = request.get_json()
    print(data['regCourseID'])
    regCourseID = data['regCourseID']
    regClassID = data['regClassID']
    regStudentID = data['regStudentID']
    if (Registration.query.filter_by(regCourseID=regCourseID, regClassID = regClassID, regStudentID = regStudentID).all()):
        return jsonify({"code": 400,"message": "The student has already been registered for this class"}), 400
    
    registration = Registration(**data)
 
    try:
        db.session.add(registration)
        db.session.commit()
    except Exception as e:
        return jsonify({"code": 500, "message": "An error occurred creating the assignment." + str(e)}), 500
 
    return jsonify({"code": 201, "data": registration.json()}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2222, debug=True)