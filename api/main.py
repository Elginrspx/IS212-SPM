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
from studentScore import *
from content import *
from progress import *

#COURSES TDD

# GET all Courses (not finalised, might want to add prereqs to return value and condition to only appear if classes are available, but this works for first sprint...?)
#used by adminCourseAssignment, home
@app.route("/courses")
def get_all_courses():
    code, data = Course.get_all_courses()
    return jsonify(
        {
            "code": code,
            "data": {
                "courses": data
            }
        }
    )

# GET Course Details By courseID 
#used by class, course, enrollClass
@app.route("/courses/<string:courseID>")
def get_course_details(courseID):
    code, data = Course.get_course_details(courseID)
    return jsonify(
                {
                    "code":code,
                    "data": {
                        "course" : data
                        }
                }
            )


#CLASSES TDD

# GET Classes by courseID
#used by AdminCourseAssignment
@app.route("/classList/<string:courseID>")
def get_course_classes(courseID):
    code, data = Class.get_course_classes(courseID)
    return jsonify(
                {
                    "code":code,
                    "data": {
                        "course" : data
                        }
                }
            )

# GET Class Details by Course-Class 
#used by class, enrollclass
@app.route("/classes/<string:courseID>/<string:classID>")
def get_class_details(courseID, classID):
    code, data = Class.get_class_details(courseID, classID)
    return jsonify(
        {
            "code":code,
            "data": {
                "course" : data
                }
        }
    )


# GET all registrations with class and student table joined
#used by course
@app.route("/classInfo/<string:courseID>", methods=["GET"])
def all_class_info(courseID):
    code, data = Class.prepare_class_details_by_course(courseID)
    for entry in data:
        print(entry)
        code, entry['noAccepted'] = Registration.get_no_accepted(entry['clsCourseID'], entry['classID'])
        print(code)
    return jsonify({"code": 200, "classInfo": data}),200

#COMPLETED TDD

# GET all completed Courses by studentID 
#used by home
@app.route("/completed/<string:ccStudentID>")
def get_students_completed_courses(ccStudentID):
    code, data = Completed.get_completed_by_student(ccStudentID)
    return jsonify(
        {
            "code": code,
            "data": {
                "courses": data
            }
        }
    )


#PREREQUISITES TDD

# GET all Prerequisites by course
#used by home
@app.route("/prereqs/<string:prereqCourseID>")
def get_course_prereq(prereqCourseID):
    code, data = Prerequisite.get_prereqs(prereqCourseID)
    return jsonify(
                {
                    "code": code,
                    "data": {
                        "courses": data
                    }
                }
            )





#REGISTRATION TDD

# GET student registrations by course
#used by adminCourseApplication
@app.route("/registration/<string:courseID>")
def get_student_registration(courseID):
    code, data = Registration.get_student_reg(courseID)
    print(data)
    for entry in data:
        code, entry['studentName'] = Student.get_name_by_id(entry['studentID'])
    return jsonify(
        {
            "code": code,
            "data": {
                "registrations": data
            }

        }
    )


# POST registration for courseClass
#used by adminCourseAssignment, enrollClass
@app.route("/registerClass", methods=['POST'])
def register_class():
    data = request.get_json()
    regCourseID = data['regCourseID']
    regClassID = data['regClassID']
    regStudentID = data['regStudentID']
    code, dataa = Registration.register_class(regCourseID, regClassID, regStudentID, data['regStatus'])
    return jsonify({"code": code,"data": dataa})


#GET list of course ID & name of those with enrolled students
#used by adminCourseApplication
@app.route("/registrationCourses", methods=["GET"])
def all_reg():
    code, data = Registration.get_enrolled_courseID()
    for entry in data:
        code, entry['courseName'] = Course.get_name_by_id(entry['regCourseID'])
    return jsonify(
        {
            "code": code,
            "courseList": data
        }
    )
    

# UPDATE registration to accepted
#used by adminCourseApplication
@app.route("/assignRegistration", methods=['PUT'])
def assign_registration():
    data = request.get_json()
    code, dataa = Registration.assign_registration(data['courseID'], data['classID'], data['studentID'])
    return jsonify(
        {
            "code": code,
            "data": dataa
        }
    )



#STUDENT TDD
# GET all students
#used by adminCourseAssignment
@app.route("/students")
def get_all_students():
    code, data = Student.get_all()
    return jsonify(
        {
            "code": code,
            "data": data
        }
    )

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

#POST questions to create quiz
@app.route("/createQuiz", methods=['POST'])
def create_quiz():
    data = request.get_json()
    code, count = Question.create_question(data)
    code1, output = Section.update_no_of_qns(data, count)
    return jsonify(
        {
            "code": code1,
            "data": output
        }
    )

#POST info to get score for questions for a quiz
#used by studentQuiz.html
@app.route("/submitQuiz/<string:qnCourseID>/<string:qnClassID>/<string:qnSectionID>", methods=['POST'])
def submit_quiz(qnCourseID, qnClassID, qnSectionID):
    output = {}
    data = request.get_json()
    studentID = data['student']
    score = Question.compute_score(data['data'], qnCourseID, qnClassID, qnSectionID)
    code, data = Score.create_score(studentID,qnCourseID, qnClassID, qnSectionID,score)
    code3, data3 = Section.get_no_qns(qnCourseID, qnClassID, qnSectionID)
    if score>.8:
        output['status'] = "Pass"
    else:
        output['status'] = "Fail"
    output['totalScore'] = data3
    return jsonify(
        {
            "code": code,
            "data": output
        }
    )


#GET class+course by trainer
@app.route("/getClassByTrainer/<string:trainer>")
def get_trainer_classes(trainer):
    code, data = Class.get_classes_by_trainer(trainer)
    for classes in data:
        code, classes["courseName"] = Course.get_name_by_id(classes['courseID'])
    return jsonify(
        {
            "code": code,
            "data": data
        }
    )

#GET class by student
@app.route("/getClassByStudent/<string:student>")
def get_student_classes(student):
    code, data = Registration.get_student_accepted_courses(student)
    for classes in data:
        code, classes["courseName"] = Course.get_name_by_id(classes['courseID'])
    return jsonify(
        {
            "code": code,
            "data": data
        }
    )

# GET all sections by course-class
@app.route("/getSections/<string:courseID>/<string:classID>")
def get_sections(courseID, classID):
    code, data = Section.get_all_sections(courseID, classID)
    return jsonify(
        {
            "code": code,
            "data": data
        }
    )

#GET all sections by course-class with status (for student side)
@app.route("/getStudentSection/<string:studentID>/<string:courseID>/<string:classID>")
def get_student_section(studentID, courseID, classID):
    code, data = Section.get_all_sections(courseID, classID)
    for content in data:
        code, content["completed"] = Progress.get_student_progress(studentID, courseID, classID, content['sectionID'])
    return jsonify(
        {
            "code": code,
            "data": data
        }
    )

#GET a student's score by section 
@app.route("/studentScore", methods=['POST'])
def get_student_score():
    output = {}
    data = request.get_json()
    code, percentage = Score.get_scores_by_student(data)
    print(percentage)
    percent = float(percentage)
    code3, maxScore = Section.get_no_qns(data['courseID'], data['classID'], data['sectionID'])
    if percent >= .8:
        output['status'] = "Pass"
        code, message = Progress.update_progress(data)
        print(message)
    else:
        output['status'] = "Fail"
    output['totalScore'] = round(percent*int(maxScore))
    output['maxScore'] = maxScore
    return jsonify(
        {
            "code": code,
            "data": output
        }
    )

#GET all section content
@app.route("/getContent/<string:courseID>/<string:classID>/<string:sectionID>")
def get_contents(courseID, classID, sectionID):
    code, data = Content.get_section_content(courseID, classID, sectionID)
    return jsonify(
        {
            "code": code,
            "data": data
        }
    )

#POST section content
@app.route("/createContent", methods=["POST"])
def create_content():
    data = request.get_json()
    code, message = Content.create_section_content(data)
    return jsonify(
        {
            "code": code,
            "data": message
        }
    )


#Score, Student, Section tdd
#get scores by section
#used by quizResults.html
@app.route("/getScores/<string:qnCourseID>/<string:qnClassID>/<string:qnSectionID>")
def get_section_scores(qnCourseID, qnClassID, qnSectionID):
    final = []
    code, data = Score.get_scores_for_sections(qnCourseID, qnClassID, qnSectionID)
    for student in data:
        # get student name
        temp = {}
        id = student["studentID"]
        code2, data2 = Student.get_student_details(id)
        #get totalScore
        code3, data3 = Section.get_no_qns(qnCourseID, qnClassID, qnSectionID)
        temp["studentName"] = data2["studentName"]
        temp["score"] = round(float(student["percentage"])*data3)
        temp["totalScore"] = data3
        temp["status"] = student["status"]
        temp["noAttempts"] = student["noAttempts"]
        final.append(temp)
    return jsonify(
        {
            "code": code,
            "data": final
        }
    )
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2222, debug=True)