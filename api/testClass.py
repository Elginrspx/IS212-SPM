#TDD code
#Email: wxlim.2019@scis.smu.edu.sg
#Full name: Lim Wei Xiang
#Student ID: 01355135

import unittest
import flask_testing

from main import app, db

from course import Course
from classs import Class

class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()
        c1 = Course(1, '3D Printing Software v1.0', 'A course on 3D printing software', False)
        c2 = Course(2, '3D Printing Software v2.0', 'A course on 3D printing software Version 2', True)
        class1 = Class(1,3, "Tan", "05-Sept-2021", "08-Sept-2023", 45, "1 Oct, 2021 to 5 Nov, 2021")
        class2 = Class(2,1, "Tan", "17-Sept-2021", "20-Sept-2023", 20, "15 Oct, 2021 to 24 Nov, 2021")
        db.session.add(c1)
        db.session.add(c2)
        db.session.add(class1)
        db.session.add(class2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class testClass(TestApp):
    def test_json(self):
        class3 = Class(2,2, "Lim", "17-Sept-2021", "20-Sept-2023", 30, "15 Oct, 2021 to 25 Nov, 2021")
        self.assertEqual(class3.json(),
        {
            "clsCourseID": 2, 
            "classID": 2, 
            "clsTrainer": "Lim", 
            "clsStartTime": "17-Sept-2021", 
            "clsEndTime": "20-Sept-2023",
            "clsLimit": 30,
            "regPeriod": "15 Oct, 2021 to 25 Nov, 2021"
        })
    
    def test_json_for_trainer(self):
        test = Class(2,2, "Lim", "17-Sept-2021", "20-Sept-2023", 30, "15 Oct, 2021 to 25 Nov, 2021")
        self.assertEqual(test.json_for_trainer(),
        {
            "courseID": 2, 
            "classID": 2, 
            "courseName": ""
        })

    def test_get_course_classes(self):
        code, data = Class.get_course_classes(2)
        self.assertEqual(data,
        [{
            "clsCourseID": '2', 
            "classID": 1, 
            "clsTrainer": "Tan", 
            "clsStartTime": "17-Sept-2021", 
            "clsEndTime": "20-Sept-2023",
            "clsLimit": 20,
            "regPeriod": "15 Oct, 2021 to 24 Nov, 2021"
        }])

    def test_get_class_details(self):
        code, data = Class.get_class_details(2,1)
        self.assertEqual(data,
        {
            "clsCourseID": '2', 
            "classID": 1, 
            "clsTrainer": "Tan", 
            "clsStartTime": "17-Sept-2021", 
            "clsEndTime": "20-Sept-2023",
            "clsLimit": 20,
            "regPeriod": "15 Oct, 2021 to 24 Nov, 2021"
        })
    
    def test_get_classes_by_trainer(self):
        code, data = Class.get_classes_by_trainer('Tan')
        self.assertEqual(data,
        [
        {
            "courseID": '1', 
            "classID": 3, 
            "courseName":""
        }, {
            "courseID": '2', 
            "classID": 1, 
            "courseName":""
        }
        ])

    def test_prep_class_details_by_course(self):
        code, data = Class.prepare_class_details_by_course(2)
        self.assertEqual(data,
        [{
            "clsCourseID": '2', 
            "classID": 1, 
            "clsTrainer": "Tan", 
            "clsStartTime": "17-Sept-2021", 
            "clsEndTime": "20-Sept-2023",
            "clsLimit": 20,
            "regPeriod": "15 Oct, 2021 to 24 Nov, 2021",
            "noAccepted":0
        }])




if __name__ == "__main__":
    unittest.main()