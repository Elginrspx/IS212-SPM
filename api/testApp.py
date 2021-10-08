import unittest
import flask_testing 
import json
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
class TestCompleted(TestApp):
    def test_Completed(self):
        #Get request dunnid request_body
        # request_body = {
        #     "ccStudentID": 1, 

        # }
        
        d1 = Completed(1, "3D Printing Hardware v1.0")
        db.session.add(d1)
        db.session.commit()
        response = self.client.get("/completed/1",
                                    content_type='application/json')
        print(response.json['data']['courses'])
        self.assertEqual(response.json['data']['courses'], [{'ccStudentID': 1, 'completedCName': '3D Printing Hardware v1.0'}])

# class TestCreateRegistration(TestApp):
#     def test_create_registration(self):
#         d1 = Registration(1, 7, 3, "enrolled")
#         # db.session.add(d1)
#         # db.session.commit()

#         request_body = {
#             "regStudentID": 1, 
#             "regCourseID": 7, 
#             "regClassID": 3, 
#             "regStatus": "enrolled"
#         }
#         response = self.client.post("/registerClass",
#                                     data=json.dumps(request_body),
#                                     content_type='application/json')
#         print(response.json['data'])
#         self.assertEqual(response.json['data'], {"regStudentID": 1, "regCourseID": "7", "regClassID": 3, "regStatus": "enrolled"}
#         )
        # d1 = Registration.query.filter_by(regStudentID = 1, regCourseID = 7, regClassID = 3)
        # db.session.delete(d1)
        # db.session.commit()
    
    # def test_create_registration_already_taken(self):

    # def test_create_registration_prereqs_not_satisfied(self):
    # def test_create_registration_already_registered(self):

#testing if it works

if __name__ == '__main__':
    unittest.main()