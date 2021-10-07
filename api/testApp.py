import unittest
import flask_testing 
import json
from app import app, db, Course, Class, Prerequisite, Student, Completed, Registration


class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/testdb'
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True
#Country roads take me home

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        # db.drop_all()

class TestCreateRegistration(TestApp):
    def test_create_registration(self):
        # d1 = Registration(1, 7, 3, "enrolled")
        # db.session.add(d1)
        # db.session.commit()

        request_body = {
            "regStudentID": 1, 
            "regCourseID": 7, 
            "regClassID": 3, 
            "regStatus": "enrolled"
        }
        response = self.client.post("/registerClass",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        print(response.json['data'])
        self.assertEqual(response.json['data'], {"regStudentID": 1, "regCourseID": "7", "regClassID": 3, "regStatus": "enrolled"}
        )
    
    # def test_create_registration_already_taken(self):

    # def test_create_registration_prereqs_not_satisfied(self):
    # def test_create_registration_already_registered(self):

#testing if it works

if __name__ == '__main__':
    unittest.main()