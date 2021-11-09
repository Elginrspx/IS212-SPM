import unittest
import flask_testing

from main import app, db

from student import Student
from completed import Completed
#TDD code
#Email: joel.seah.2019@scis.smu.edu.sg
#Full name: Seah Shang Hong, Joel
#Student ID: 01372086
class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()
        s1 = Student(1,"Selena Gomez", "junior intern")
        s2 = Student(3,"Leeroy Jenkins", "junior intern")
        c1 = Completed("1","3D Printing Software v2.0")
        db.session.add(c1)
        db.session.add(s1)
        db.session.add(s2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class testStudent(TestApp):
    def test_json(self):
        s1 = Student(2,"Justin Bieber", "junior intern")
        self.assertEqual(s1.json(),{
            "studentID":2,
            "studentName":"Justin Bieber",
            "sPosition":"junior intern"
        })

    def test_get_student_details(self):
        code, data = Student.get_student_details(1)
        self.assertEqual(data, {
            "studentID":1,
            "studentName":"Selena Gomez",
            "sPosition":"junior intern"
        })

    def test_get_all(self):
        code, data = Student.get_all()
        self.assertEqual(data, [{
            "studentID":1,
            "studentName":"Selena Gomez",
            "sPosition":"junior intern"
        },{
            "studentID":3,
            "studentName":"Leeroy Jenkins",
            "sPosition":"junior intern"
        }])
    
    def test_get_name_by_id(self):
        code, data = Student.get_name_by_id(3)
        self.assertEqual(data,'Leeroy Jenkins')

class testCompleted(TestApp):
    def test_json(self):
        c2 = Completed("3","3D Printing Software v2.0")
        self.assertEqual(c2.json(),{
        "ccStudentID": '3', 
        "completedCName": "3D Printing Software v2.0"
        })

    def test_get_students_completed(self):
        code, data = Completed.get_completed_by_student(1)
        self.assertEqual(data, [{
        "ccStudentID": 1, 
        "completedCName": "3D Printing Software v2.0"
        }])

    

if __name__ == "__main__":
    unittest.main()