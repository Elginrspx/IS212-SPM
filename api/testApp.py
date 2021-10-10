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

    def tearDown(self):
        db.session.remove()
        # db.drop_all()

class TestCreateCourse(TestApp):
    def test_get_course(self):
        response = self.client.get("/courses")
        self.assertEqual(response.json['code'], 200)

    def test_get_course_by_id(self):
        response = self.client.get("/courses/1")
        self.assertEqual(response.json['code'], 200)

class TestCreatePrereq(TestApp):
    def test_get_prereq_by_courseid(self):
        response = self.client.get("/prereqs/3")
        self.assertEqual(response.json['code'], 200)

if __name__ == '__main__':
    unittest.main()