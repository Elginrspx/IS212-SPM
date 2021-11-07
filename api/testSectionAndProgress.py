import unittest
import flask_testing

from main import app, db

from course import Course
from classs import Class
from section import Section
from progress import Progress

class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()
        dummyCourse = Course(1, '3D Printing Software v1.0', 'A course on 3D printing software', False)
        dummyClass2 = Class(1,3, "Tan", "05-Sept-2021", "08-Sept-2023", 45, "1 Oct, 2021 to 5 Nov, 2021")
        dummySection = Section(1,3,"1","Introduction to Printing", 1)
        dummySection2 = Section(1,3,"2", "Working with Printers", 1)
        dummyProgress = Progress(1, 1, 3, 1, "true")
        dummyProgress2 = Progress(1, 1, 3, 2, "false")
        db.session.add(dummyCourse)
        db.session.add(dummyClass2)
        db.session.add(dummySection)
        db.session.add(dummySection2)
        db.session.add(dummyProgress)
        db.session.add(dummyProgress2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class testSection(TestApp):
    def test_json(self):
        s1 = Section(1,3,1,"Introduction to Printing",1)
        self.assertEqual(s1.json(),{
            "secCourseID" : 1,
            "secClassID": 3,
            "sectionID" : 1,
            "sectionName": "Introduction to Printing",
            "noOfQns": 1
        })

    def test_json_section_info(self):
        s2 = Section(1,3,1,"Introduction to Printing",1)
        self.assertEqual(s2.json_section_info(),{
            "sectionID" : 1,
            "sectionName": "Introduction to Printing"
        })

    def test_get_all_sections(self):
        code, data = Section.get_all_sections(1, 3)
        self.assertEqual(data,[{
            "sectionID" : '1',
            "sectionName": "Introduction to Printing"
        }, {
            "sectionID" : '2',
            "sectionName": "Working with Printers"
        }])

    def test_get_no_qns(self):
        code, data = Section.get_no_qns(1,3,1)
        self.assertEqual(data,1)

    def test_update_no_qns(self):
        data = {'data': [{
            'qnCourseID':'1',
            'qnClassID':3,
            'qnSectionID':'1'
            }]}
        code, msg = Section.update_no_of_qns(data, 3)
        self.assertEqual(msg,"update success")

class testProgress(TestApp):
    def test_get_student_progress(self):
        code, data = Progress.get_student_progress(1, 1, 3, 1)
        self.assertEqual(data,'true')

    def test_update_progress(self):
        data = {
            'studentID':1,
            'courseID':1,
            'classID':3,
            'sectionID':1
        }
        code, output = Progress.update_progress(data)
        self.assertEqual(output,"Updated Successfully")

if __name__ == "__main__":
    unittest.main()