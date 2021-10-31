from main import db
from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKeyConstraint
from classs import Class


class Section(db.Model):
    __tablename__ = 'sections'

    secCourseID = db.Column(db.String(30), primary_key=True)
    secClassID = db.Column(db.Integer, nullable=False, primary_key=True)
    sectionID = db.Column(db.String(30), nullable=False, primary_key=True)
    sectionName = db.Column(db.String(100), nullable=False)
    noOfQns = db.Column(db.Integer, nullable=False)
    
    __table_args__ = (ForeignKeyConstraint([secCourseID, secClassID],
                    [Class.clsCourseID, Class.classID]),
                      {})
    classSection = db.relationship(
    'Class', primaryjoin='and_(Class.classID == Section.secClassID, Class.clsCourseID == Section.secCourseID)', backref='sections')

    def __init__(self, secCourseID, secClassID, sectionID, sectionName, noOfQns):
        self.secCourseID = secCourseID
        self.secClassID = secClassID
        self.sectionID = sectionID
        self.sectionName = sectionName
        self.noOfQns = noOfQns

    def json_section_info(self):
        return {
            "sectionID" : self.sectionID,
            "sectionName": self.sectionName
        }

    def json(self):
        return {
            "secCourseID" : self.secCourseID,
            "secClassID": self.secClassID,
            "sectionID" : self.sectionID,
            "sectionName": self.sectionName,
            "noOfQns": self.noOfQns
        }
    
    def get_all_sections(courseID, classID):
        try:
            sectionList = Section.query.filter_by(secCourseID=courseID, secClassID=classID).all()
            if sectionList:
                return 200, [section.json_section_info() for section in sectionList]
        except Exception as e:
            return 404, "No sections found" + str(e)

    def get_no_qns(secCourseID, secClassID, sectionID):
        noQns = db.session.query(Section.noOfQns).filter(Section.secCourseID== secCourseID, Section.secClassID == secClassID, Section.sectionID == sectionID).first()
        data = noQns[0]
        return 200, data

    def update_no_of_qns(data, count):
        data = data['data']
        data2 = data[0]
        try:
            toUpdate = Section.query.filter_by(secCourseID = data2['qnCourseID'], secClassID =data2['qnClassID'],sectionID = data2['qnSectionID']).first()
            toUpdate.noOfQns = count
            db.session.commit()
            return 201, "update success"
        except Exception as e:
            return 500, "could not update number of questions. "+str(e)