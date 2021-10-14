from main import db

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

