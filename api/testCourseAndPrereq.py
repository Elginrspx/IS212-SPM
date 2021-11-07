# Name: Toh Ying Hui
# Email: yinghui.toh.2019@scis.smu.edu.sg
# Student ID: 01382178

import unittest
import flask_testing

from main import app, db

from course import Course
from prerequisite import Prerequisite

class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()
        dummyCourse = Course(1, '3D Printing Software v1.0', 'A course on 3D printing software', False)
        dummyCourse2 = Course(2, '3D Printing Software v2.0', 'A course on 3D printing software Version 2', True)
        dummyPrerequisite = Prerequisite(2, "3D Printing Software v1.0")
        db.session.add(dummyCourse)
        db.session.add(dummyCourse2)
        db.session.add(dummyPrerequisite)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class testCourse(TestApp):
    def test_json(self):
        c1 = Course(1, "New Course", "a very helpful course", False)
        self.assertEqual(c1.json(), {
            "courseID" : 1,
            "courseName" : "New Course",
            "cDescription" : "a very helpful course",
            "have": False
        })
    
    def test_get_course_details(self):
        code, data = Course.get_course_details(1)
        self.assertEqual(data, {
            "courseID" : '1',
            "courseName" : '3D Printing Software v1.0',
            "cDescription" : 'A course on 3D printing software',
            "have": False
        })

    def test_get_all_courses(self):
        code, data = Course.get_all_courses()
        self.assertEqual(data, [{
            "courseID" : '1',
            "courseName" : '3D Printing Software v1.0',
            "cDescription" : 'A course on 3D printing software',
            "have": False
        },{
            "courseID" : '2',
            "courseName" : '3D Printing Software v2.0',
            "cDescription" : 'A course on 3D printing software Version 2',
            "have": True
        }])

    def test_get_name_by_id(self):
        code, name = Course.get_name_by_id(1)
        self.assertEqual(name, '3D Printing Software v1.0')

class testPrereq(TestApp):
    def test_json(self):
        p1 = Prerequisite(2, "3D Printing Software v1.0")
        self.assertEqual(p1.json(),{
            "prereqCourseID" : 2,
            "prereqName" : "3D Printing Software v1.0"
        })

    def test_get_prereqs(self):
        code, data = Prerequisite.get_prereqs(2)
        self.assertEqual(data,[{
            "prereqCourseID" : '2',
            "prereqName" : "3D Printing Software v1.0"
        }])

if __name__ == "__main__":
    unittest.main()