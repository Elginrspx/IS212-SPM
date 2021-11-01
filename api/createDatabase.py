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
from content import Content
from progress import Progress

db.drop_all()
db.create_all()

dummyCourse = Course(1, '3D Printing Software v1.0', 'A course on 3D printing software', '3D Printing Basics, 3D Printer Software Installation', False)
dummyCourse2 = Course(2, '3D Printing Software v2.0', 'A course on 3D printing software Version 2', '3D Printing Advanced', True)
dummyClass = Class(1,2, "Tan", "05-Sept-2021", "08-Sept-2023", 45, "1 Oct, 2021 to 5 Nov, 2021")
dummyClass2 = Class(1,3, "Lim Ah Hock", "12-Sept-2021", "14-Sept-2023", 35, "9 Oct, 2021 to 9 Nov, 2021")
dummyClass3 = Class(2,1, "Tan", "17-Sept-2021", "20-Sept-2023", 20, "15 Oct, 2021 to 24 Nov, 2021")
dummyUserReg = Registration("1","1","3","accepted")
dummyUserReg2 = Registration("2","1","3","enrolled")
dummyUserReg3 = Registration("3","2","1","enrolled")
dummyUserReg4 = Registration("1","2","1","accepted")
dummyPrerequisite = Prerequisite(2, "3D Printing Software v1.0")
dummySection = Section(1,3,"1","Introduction to Printing", 3)
dummySection2 = Section(1,3,"2", "Working with Printers", 3)
dummySection3 = Section(1,3,"3", "Conclusion to Printing", 3)
dummyStudent = Student(1,"Justin Bieber", "junior intern")
dummyStudent2 = Student(2,"Selena Gomez", "junior intern")
dummyStudent3 = Student(3,"Leeroy Jenkins", "junior intern")
dummyCompleted = Completed("1","3D Printing Software v2.0")
dummyQN1 = Question(1,3,"2", "Test question with multiple answers", "Answer 1,Answer 2", "Answer 1,Answer 2,Answer 3,Answer 4", "true")
dummyQN2 = Question(1,3,"2", "How long it takes to fix a printer?", "1 Minute", "1 Minute,5 Minute, 10 Minute, 20 Minute", "false")
dummyQN3 = Question(1,3,"2", "Sample True False Question", "True", "True,False", "false")
dummyQN4 = Question(1,3,"1", "Test question with multiple answers", "Answer 1,Answer 2", "Answer 1,Answer 2,Answer 3,Answer 4", "true")
dummyQN5 = Question(1,3,"1", "How long it takes to fix a printer?", "1 Minute", "1 Minute,5 Minute, 10 Minute, 20 Minute", "false")
dummyQN6 = Question(1,3,"1", "Sample True False Question", "True", "True,False", "false")
dummyQN7 = Question(1,3,"3", "Test question with multiple answers", "Answer 1,Answer 2", "Answer 1,Answer 2,Answer 3,Answer 4", "true")
dummyQN8 = Question(1,3,"3", "How long it takes to fix a printer?", "1 Minute", "1 Minute,5 Minute, 10 Minute, 20 Minute", "false")
dummyQN9 = Question(1,3,"3", "Sample True False Question", "True", "True,False", "false")
dummyScore1 = Score(1,1,3,"2", ".80", 1)
dummyScore2 = Score(2,1,3,"2", ".70", 3)
dummyContent = Content(1, 3, 1, 1, "Introduction Video", "video", "https://youtu.be/dQw4w9WgXcQ")
dummyContent2 = Content(1, 3, 2, 1, "Printer Tutorial", "document", "https://docs.google.com/document/d/1tlscRf-i1XFj_XfBA3L52arAm8UDNEJOnRgAPr8luMw/edit?usp=sharing")
dummyContent3 = Content(1, 3, 3, 1, "Printer Slides", "powerpoint", "https://docs.google.com/presentation/d/1wF_C8ZO1Quk1LfP7IefjWeKjeZrhx5j50ZzjtbV0Ibo/edit?usp=sharing")
dummyProgress1 = Progress(1, 1, 3, 1, "true")
dummyProgress2 = Progress(1, 1, 3, 2, "false")
dummyProgress3 = Progress(1, 1, 3, 3, "false")

db.session.add(dummyCourse)
db.session.add(dummyCourse2)
db.session.add(dummyClass)
db.session.add(dummyClass2)
db.session.add(dummyClass3)
db.session.add(dummyUserReg)
db.session.add(dummyUserReg2)
db.session.add(dummyUserReg3)
db.session.add(dummyUserReg4)
db.session.add(dummyPrerequisite)
db.session.add(dummySection)
db.session.add(dummySection2)
db.session.add(dummySection3)
db.session.add(dummyStudent)
db.session.add(dummyStudent2)
db.session.add(dummyStudent3)
db.session.add(dummyCompleted)
db.session.add(dummyQN3)
db.session.add(dummyQN1)
db.session.add(dummyQN2)
db.session.add(dummyScore1)
db.session.add(dummyScore2)
db.session.add(dummyContent)
db.session.add(dummyContent2)
db.session.add(dummyContent3)
db.session.add(dummyProgress1)
db.session.add(dummyProgress2)
db.session.add(dummyProgress3)
db.session.commit()