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
from course import *
from classs import *
from completed import *
from prerequisite import *
from registration import *
from student import *
from question import *


#COURSES TDD

# GET all Courses (not finalised, might want to add prereqs to return value and condition to only appear if classes are available, but this works for first sprint...?)
#used by adminCourseAssignment, home
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

# GET Course Details By courseID 
#used by class, course, enrollClass
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



#CLASSES TDD

# GET Classes by courseID
#used by AdminCourseAssignment
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
#used by class, enrollclass
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

# GET all registrations with class and student table joined
#used by course
@app.route("/classInfo/<string:courseID>", methods=["GET"])
def all_class_info(courseID):
    try:
        # test = db.session.query(func.count('*').group_by(Registration.regCourseID, Registration.regClassID), Registration.regCourseID, Registration.regClassID, Student.studentName).join(Class, and_(Class.classID == Registration.regClassID, Class.clsCourseID == Registration.regCourseID)).join(Student, Student.studentID == Registration.regStudentID).all()
        classList = db.session.query(Class.clsCourseID, Class.classID, Class.clsTrainer, Class.clsStartTime, Class.clsEndTime, Class.clsLimit, Class.regPeriod).filter(Class.clsCourseID==courseID).all()
        # Class.query.filter_by(clsCourseID=courseID).all()        # print(test)

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

#COMPLETED TDD

# GET all completed Courses by studentID 
#used by home
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


#PREREQUISITES TDD

# GET all Prerequisites by course
#used by home
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




#REGISTRATION TDD

# GET student registrations by course
#used by adminCourseApplication
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
#used by adminCourseAssignment, enrollClass
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
#used by adminCourseApplication
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


# UPDATE registration to accepted
#used by adminCourseApplication
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


# GET all eligible courses by user
#create four tables. 1)taken  2)all  3)eligible  4)prereqs
#may be needed for sprint 4 adminCourseAssignment
#COURSE integration
@app.route("/eligibleCourses/<string:userID>")
def get_eligible_courses(userID):
    taken = []
    all = []
    eligible = {}
    prereqs = {}

    #query for table population
    courses = db.session.query(Course.courseID, Course.courseName).all()
    took = db.session.query(Completed.completedCName).filter(userID==Completed.ccStudentID).all()
    havePrereq = db.session.query(Prerequisite.prereqCourseID, Prerequisite.prereqName).all()

    #populate lists of all, taken, and prerequisite courses
    for course in courses:
        all.append(course)
    for course in took:
        taken.append(course[0])
    for each in havePrereq:
        if each[0] in prereqs:
            prereqs[each[0]].append(each[1])
        else:
            prereqs[each[0]] = []
            prereqs[each[0]].append(each[1])

    #algo to compute list of eligible courses

    for id, name in all:
        if name in taken:
            pass
        elif id in prereqs:
            check = True
            for c in prereqs[id]:
                # print(c)
                if c not in taken:
                    check=False
            if check:    
                eligible[id]=name
        else:
            eligible[id]=name
    return eligible

#STUDENT TDD
# GET all students
#used by adminCourseAssignment
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

#QUESTION TDD
#GET all questions for a quiz
#used by studentQuiz.html
@app.route("/questions/<string:qnCourseID>/<string:qnClassID>/<string:qnSectionID>")
def get_questions(qnCourseID, qnClassID, qnSectionID):
    print("work")
    code, data = Question.get_questions(qnCourseID, qnClassID, qnSectionID)
    return jsonify(
        {
            "code": code,
            "data": data
        }
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2222, debug=True)