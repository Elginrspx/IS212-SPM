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
        db.reflect()
        db.drop_all()


#For registration
class TestCreateRegistration(TestApp):
    def test_create_registration(self):
        d1 = Course(1, '3D Printing Software v1.0', 'A course on 3D printing software', '3D Printing Basics, 3D Printer Software Installation', False)
        d2 = Class(1,3, "Lim Ah Hock", "12-Sept-2021", "14-Sept-2023", 35, "9 Oct, 2021 to 9 Nov, 2021")
        db.session.add(d1)
        db.session.add(d2)
        db.session.commit()

        request_body = {
            "regStudentID": 1, 
            "regCourseID": 1, 
            "regClassID": 3, 
            "regStatus": "enrolled"
        }
        response = self.client.post("/registerClass",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        print(response.json)
        self.assertEqual(response.json['data'], {"regStudentID": 1, "regCourseID": "1", "regClassID": 3, "regStatus": "enrolled"}
        )
    
    # def test_create_registration_already_taken(self):

    # def test_create_registration_prereqs_not_satisfied(self):
    # def test_create_registration_already_registered(self):

#testing if it works

if __name__ == '__main__':
    unittest.main()