from main import db
from sqlalchemy import *

class Course(db.Model):
    __tablename__ = 'courses'

    courseID = db.Column(db.String(30), primary_key=True)
    courseName = db.Column(db.String(30), nullable = False)
    cDescription = db.Column(db.Text, nullable=False)
    cOutline = db.Column(db.Text, nullable=False)
    have = db.Column(db.Boolean, nullable = False)

    def __init__(self, courseID, courseName, cDescription, cOutline, have):
        self.courseID = courseID
        self.courseName = courseName
        self.cDescription = cDescription
        self.cOutline = cOutline
        self.have = have

    def json(self):
        return {
            "courseID" : self.courseID,
            "courseName" : self.courseName,
            "cDescription" : self.cDescription,
            "cOutline" : self.cOutline,
            "have": self.have
        }

    def get_course_details(courseID):
        try: 
            course = Course.query.filter_by(courseID=courseID).first()
            if course:
                return 200, course.json()
        except Exception as e:
            return 404, "Course not available"
    
    def get_all_courses():
        try:
            courseList = Course.query.all()
            
            if len(courseList):
                return 200, [course.json() for course in courseList]

        except Exception as e:
            return 404, "There are no courses." + str(e)

    def get_name_by_id(id):
        try: 
            course = db.session.query(Course.courseName).filter(Course.courseID== id).first()
            data = course[0]
            return 200, data
        except Exception as e:
            return 404, "Course not available"


