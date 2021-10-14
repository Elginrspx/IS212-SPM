from main import db


class Prerequisite(db.Model):
    __tablename__ = 'prerequisites'

    prereqCourseID = db.Column(db.String(30), db.ForeignKey('courses.courseID', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    prereqName = db.Column(db.String(30), primary_key=True)

    coursePrereq = db.relationship(
    'Course', primaryjoin='Prerequisite.prereqCourseID == Course.courseID', backref='prerequisites')

    def __init__(self, prereqCourseID, prereqName):
        self.prereqCourseID = prereqCourseID
        self.prereqName = prereqName

    def json(self):
        return {
            "prereqCourseID" : self.prereqCourseID,
            "prereqName" : self.prereqName
        }