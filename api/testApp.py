import unittest
import flask_testing 
import json
from unittest import mock
from app import app, db, Course, Class, Prerequisite, Student, Completed, Registration


class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/testdb'
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()
        dummyCourse = Course(1, '3D Printing Software v1.0', 'A course on 3D printing software', '3D Printing Basics, 3D Printer Software Installation', False)
        dummyCourse2 = Course(2, '3D Printing Software v2.0', 'A course on 3D printing software Version 2', '3D Printing Advanced', True)
        dummyClass = Class(1,3, "Lim Ah Hock", "12-Sept-2021", "14-Sept-2023", 35, "9 Oct, 2021 to 9 Nov, 2021")
        dummyUserReg = Registration(1,1,3,"enrolled")
        dummyPrerequisite = Prerequisite(2, "3D Printing Software v2.0")
        db.session.add(dummyCourse)
        db.session.add(dummyCourse2)
        db.session.add(dummyClass)
        db.session.add(dummyUserReg)
        db.session.add(dummyPrerequisite)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestCreateCourse(TestApp):
    def test_get_course(self):
        response = self.client.get("/courses")
        print(response.json['data'])
        self.assertEqual(response.json['code'], 200)

    def test_get_course_by_id(self):
        response = self.client.get("/courses/1")
        self.assertEqual(response.json['code'], 200)

    #[Feature does not exist yet]
    def test_create_course(self):
        request_body = {
            "courseID": 100, 
            "courseName": "Test Name", 
            "cDescription": "Test Description", 
            "cOutline": "Test Outline",
            "have": 0
        }
        response = self.client.post("/courses",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json['data'], {"courseID": 100, "courseName": "Test Name", "cDescription": "Test Description", "cOutline": "Test Outline", "have": 0})

class TestCreatePrereq(TestApp):
    def test_get_prereq_by_courseid(self):
        response = self.client.get("/prereqs/2")
        self.assertEqual(response.json['code'], 200)

    #[Feature does not exist yet]
    # CourseID 100 exist, prerequisite should be created successfully
    def test_create_prerequisites(self):
        request_body = {
            "prereqCourseID": 100, 
            "prereqCourseID": "Test Name"
        }
        response = self.client.post("/prerequisites",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json['data'], {"prereqCourseID": 100, "prereqCourseID": "Test Name"})

    #[Feature does not exist yet]
    # CourseID 101 does NOT exist, prerequisite should NOT be created successfully
    # @edena i assume there shld be some backend logic
    def test_create_prerequisites(self):
        request_body = {
            "prereqCourseID": 101, 
            "prereqCourseID": "Test Failure"
        }
        response = self.client.post("/prerequisites",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json['code'], 400)

class TestRegistration(TestApp):
    def test_force_update_registration_success(self):
        request_body = {
            "regStudentID": 1, 
            "regCourseID": 1, 
            "regClassID": 3, 
            "regStatus": "assigned"
        }
        response = self.client.post("/registerClass",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        print(response.json)
        self.assertEqual(response.json['data'], {"regStudentID": 1, "regCourseID": "1", "regClassID": 3, "regStatus": "assigned"})

    def test_force_create_registration_wDiff_Class_success(self):
        request_body = {
            "regStudentID": 1, 
            "regCourseID": 2, 
            "regClassID": 3, 
            "regStatus": "assigned"
        }
        response = self.client.post("/registerClass",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        print(response.json)
        self.assertEqual(response.json['data'], {"regStudentID": 1, "regCourseID": "2", "regClassID": 3, "regStatus": "assigned"})
        #create one more self.assert to check if it was deleted/updated

    def test_student_create_new_registration_success(self):
        request_body = {
            "regStudentID": 2, 
            "regCourseID": 1, 
            "regClassID": 3, 
            "regStatus": "enrolled"
        }
        response = self.client.post("/registerClass",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        print(response.json)
        self.assertEqual(response.json['data'], {"regStudentID": 2, "regCourseID": "1", "regClassID": 3, "regStatus": "enrolled"})

class TestCompleted(TestApp):
#Test if we are able to get the data if we create it
    def test_Completed(self):
        s1 = Student(1, 'Lim Ah Hock', 'Repair Engineer (Senior)')
        d1 = Completed(1, "3D Printing Hardware v1.0")
        db.session.add(d1)
        db.session.add(s1)
        db.session.commit()
        response = self.client.get("/completed/1",
                                    content_type='application/json')
        print(response.json['code'])
        self.assertEqual(response.json['data']['courses'], [{'ccStudentID': 1, 'completedCName': '3D Printing Hardware v1.0'}])

if __name__ == '__main__':
    unittest.main()