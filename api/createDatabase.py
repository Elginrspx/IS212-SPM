from main import db

from course import Course
from classs import Class
from completed import Completed
from prerequisite import Prerequisite
from registration import Registration
from student import Student
from section import Section
from question import Question
from studentScore import Score


db.drop_all()
db.create_all()

dummyCourse = Course(1, '3D Printing Software v1.0', 'A course on 3D printing software', '3D Printing Basics, 3D Printer Software Installation', False)
dummyCourse2 = Course(2, '3D Printing Software v2.0', 'A course on 3D printing software Version 2', '3D Printing Advanced', True)
dummyClass = Class(1,3, "Lim Ah Hock", "12-Sept-2021", "14-Sept-2023", 35, "9 Oct, 2021 to 9 Nov, 2021")
dummyUserReg = Registration("1","1","3","enrolled")
dummyPrerequisite = Prerequisite(2, "3D Printing Software v1.0")
dummySection = Section(1,3,"Chapter2", 3)
dummyStudent = Student(1,"Justin Bieber", "junior intern")
dummyStudent2 = Student(2,"Selena Gomez", "junior intern")
dummyStudent3 = Student(3,"meep", "junior intern")
dummyQN1 = Question(1,3,"Chapter2", "What is the answer", "the answer", "Answer, theanswer, the answer, ans", "true")
dummyQN2 = Question(1,3,"Chapter2", "What is the answer now", "ans", "Answers, theanswers, the answers, ans", "true")
dummyQN3 = Question(1,3,"Chapter2", "What is the answer teehee", "Answer", "Answer, theanswer, the answer, ans", "false")
dummyScore1 = Score(1,1,3,"Chapter2", .80, 1)
dummyScore2 = Score(2,1,3,"Chapter2", .70, 3)
dummyScore3 = Score(3,1,3,"Chapter2", .80, 1)
db.session.add(dummyCourse)
db.session.add(dummyCourse2)
db.session.add(dummyClass)
db.session.add(dummyUserReg)
db.session.add(dummyPrerequisite)
db.session.add(dummySection)
db.session.add(dummyStudent)
db.session.add(dummyStudent2)
db.session.add(dummyStudent3)
db.session.add(dummyQN3)
db.session.add(dummyQN1)
db.session.add(dummyQN2)
db.session.add(dummyScore1)
db.session.add(dummyScore2)
db.session.add(dummyScore3)
db.session.commit()




