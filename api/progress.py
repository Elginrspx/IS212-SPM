from main import db
from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKeyConstraint
from section import Section



class Progress(db.Model):
    __tablename__ = 'progress'

    progStudentID = db.Column(db.String(30), primary_key=True)
    progCourseID = db.Column(db.String(30), primary_key=True)
    progClassID = db.Column(db.Integer, nullable=False, primary_key=True)
    progSectionID = db.Column(db.String(30), nullable=False, primary_key=True)
    done = db.Column(db.String(5), nullable=False)

    __table_args__ = (ForeignKeyConstraint([progCourseID, progClassID, progSectionID],
                    [Section.secCourseID, Section.secClassID, Section.sectionID]),
                      {})
    sectionProgress = db.relationship(
    'Section', primaryjoin='and_(Section.secCourseID==Progress.progCourseID, Section.secClassID==Progress.progClassID, Section.sectionID==Progress.progSectionID)', backref='progress')

    def __init__(self, progStudentID, progCourseID, progClassID, progSectionID, done):
        self.progStudentID = progStudentID
        self.progCourseID = progCourseID
        self.progClassID = progClassID
        self.progSectionID = progSectionID
        self.done = done

    def get_student_progress(studentID, courseID, classID, sectionID):
        try:
            status = db.session.query(Progress.done).filter(Progress.progStudentID==studentID, Progress.progCourseID==courseID, Progress.progClassID==classID, Progress.progSectionID==sectionID).first()
            data = status[0]
            return 200, data
        except Exception as e:
            return 400, "No content found. " + str(e)

    def update_progress(data):
        try: 
            data['sectionID'] = int(data['sectionID']) + 1
            toUpdate = Progress.query.filter_by(progStudentID = data['studentID'], progCourseID =  data['courseID'], progClassID = data['classID'], progSectionID = data['sectionID']).first()
            toUpdate.done = "true"
            db.session.commit()
            return 201, "Updated Successfully"
        except Exception as e:
            return 500, "There was an error updating. " + str(e)
        