import unittest
import flask_testing
import json
from main import app, db
from sqlalchemy import *
from course import Course
from classs import Class
from registration import Registration

class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        db.drop_all()
        db.create_all()
        c1 = Course(1, '3D Printing Software v1.0', 'A course on 3D printing software', '3D Printing Basics, 3D Printer Software Installation', False)
        c2 = Course(2, '3D Printing Software v2.0', 'A course on 3D printing software Version 2', '3D Printing Advanced', True)
        class1 = Class(1,3, "Tan", "05-Sept-2021", "08-Sept-2023", 45, "1 Oct, 2021 to 5 Nov, 2021")
        class2 = Class(2,1, "Tan", "17-Sept-2021", "20-Sept-2023", 20, "15 Oct, 2021 to 24 Nov, 2021")
        r1 = Registration(1, 1, 3, "enrolled")
        r2 = Registration("2","1","3","accepted")
        r3 = Registration("3","2","1","enrolled")
        db.session.add(c1)
        db.session.add(c2)
        db.session.add(class1)
        db.session.add(class2)
        db.session.add(r1)
        db.session.add(r2)
        db.session.add(r3)
        db.session.commit()
    # def tearDown(self):
    #     db.session.remove()
    #     db.drop_all()

class testRegistration(TestApp):
        
    def test_assign_reg(self):
        code, data = Registration.assign_registration(1,3,1)
        self.assertEqual(data['regStatus'], "accepted")

    # def test_get_student_accepted_courses(self):
    #     code, data = Registration.get_student_accepted_courses(2)
    #     self.assertEqual(data[0]['courseID'], '1')
    #     self.assertEqual(data[0]['classID'], 3)
    #     self.assertEqual(data[0]['courseName'], '')

    # def test_get_no_accepted(self):
    #     code, data = Registration.get_no_accepted(1,3)
    #     self.assertEqual(data, 1)

    # def test_get_student_reg(self):
    #     code, data = Registration.get_student_reg(1)
    #     self.assertEqual(data, [{"regCourseID":'1', "regClassID":3, "studentName":'','clsLimit':45, 'studentID':1, 'taken': 1}])

    # def test_get_enrolled_course(self):
    #     code, data = Registration.get_enrolled_courseID()
    #     self.assertEqual(data, [{'regCourseID':'1', 'courseName':''},{'regCourseID':'2', 'courseName':''}])



if __name__ == "__main__":
    unittest.main()
