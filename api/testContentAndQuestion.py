#Created By: Elgin Seow

import unittest
import flask_testing

from main import app, db

from course import Course
from classs import Class
from section import Section
from content import Content
from question import Question

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
        dummySection3 = Section(1,3,"3", "Conclusion to Printing", 1)
        dummyQN1 = Question(1,3,"2", "Test question with multiple answers", "Answer 1,Answer 2", "Answer 1,Answer 2,Answer 3,Answer 4", "true")
        dummyQN2 = Question(1,3,"1", "This quiz is simple", "False", "True,False", "false")
        dummyQN3 = Question(1,3,"3", "Maintenance require which tools", "Screwdriver,Wrench", "Screwdriver,Coffee,Spoon,Wrench", "true")
        dummyContent = Content(1, 3, 1, 1, "Introduction Video", "vid", "https://youtu.be/dQw4w9WgXcQ")
        dummyContent2 = Content(1, 3, 2, 1, "Printer Tutorial", "doc", "https://docs.google.com/document/d/1tlscRf-i1XFj_XfBA3L52arAm8UDNEJOnRgAPr8luMw/edit?usp=sharing")
        dummyContent3 = Content(1, 3, 3, 1, "Printer Slides", "ppt", "https://docs.google.com/presentation/d/1wF_C8ZO1Quk1LfP7IefjWeKjeZrhx5j50ZzjtbV0Ibo/edit?usp=sharing")
        db.session.add(dummyCourse)
        db.session.add(dummyClass2)
        db.session.add(dummySection)
        db.session.add(dummySection2)
        db.session.add(dummySection3)
        db.session.add(dummyQN1)
        db.session.add(dummyQN2)
        db.session.add(dummyQN3)
        db.session.add(dummyContent)
        db.session.add(dummyContent2)
        db.session.add(dummyContent3)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class testContent(TestApp):
    def test_json(self):
        c1 = Content(2, 2, 1, 1, "Introduction Video", "vid", "https://youtu.be/dQw4w9WgXcQ")
        self.assertEqual(c1.json(),{
            "contentID": 1,
            "name": "Introduction Video",
            "doctype": "vid",
            "link": "https://youtu.be/dQw4w9WgXcQ"
        })

    def test_get_section_content(self):
        code, data = Content.get_section_content(1,3,1)
        self.assertEqual(data,[{
            "contentID": "1",
            "name": "Introduction Video",
            "doctype": "vid",
            "link": "https://youtu.be/dQw4w9WgXcQ"
        }])

    def test_create_section_content(self):
        input = {"data":[{
            "courseID":1,
            "classID":3,
            "sectionID":1,
            "contentID": 2,
            "contentName": "The Real Content Video",
            "doctype": "vid",
            "link": "https://youtu.be/dQw4w9WgXcQ"
        }]}
        code, data = Content.create_section_content(input)
        self.assertEqual(data,"Content created")

class testQuestion(TestApp):
    def test_json(self):
        q1 = Question(1,3,"3", "Do you love SPM?", "True", "True,False", "false")
        self.assertEqual(q1.json(),{
            "qnCourseID" : 1,
            "qnClassID": 3,
            "qnSectionID" : '3',
            "question": "Do you love SPM?",
            "answer": "True",
            "choices": "True,False",
            "isMultiple": "false"
        })

    def test_get_questions(self):
        code, data = Question.get_questions(1,3,3)
        self.assertEqual(data,[{
            "question": "Maintenance require which tools", 
            "answer": "Screwdriver,Wrench",
            "choices": "Screwdriver,Coffee,Spoon,Wrench",
            "isMultiple": "true"
        }])

    def test_compute_score(self):
        data = [{
            "qn": "Maintenance require which tools", 
            "ans": "Screwdriver,Wrench"
            }]
        output = Question.compute_score(data, 1, 3, 3)
        self.assertEqual(output,1)
    
    def test_create_question(self):
        data = {"data" : [{
            "qnCourseID" : 1,
            "qnClassID": 3,
            "qnSectionID" : '3',
            "question": "Do you love SPM?",
            "answer": "True",
            "choices": "True,False",
            "isMultiple": "false"
            },{
            "qnCourseID" : 1,
            "qnClassID": 3,
            "qnSectionID" : '3',
            "question": "Maintenance require which tools", 
            "answer": "Screwdriver,Wrench",
            "choices": "Screwdriver,Coffee,Spoon,Wrench",
            "isMultiple": "true"
            }]}
        code, msg = Question.create_question(data)
        self.assertEqual(msg,"Creation Successful")

if __name__ == "__main__":
    unittest.main()