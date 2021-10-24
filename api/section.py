from main import db


class Section(db.Model):
    __tablename__ = 'sections'

    secCourseID = db.Column(db.Integer, primary_key=True)
    secClassID = db.Column(db.String(30), nullable=False)
    sectionID = db.Column(db.String(30))
    noOfQns = db.Column(db.Integer)


    def __init__(self, secCourseID, secClassID, sectionID, noOfQns):
        self.secCourseID = secCourseID
        self.secClassID = secClassID
        self.sectionID = sectionID
        self.noOfQns = noOfQns


    def json(self):
        return {
            "secCourseID" : self.secCourseID,
            "secClassID": self.secClassID,
            "sectionID" : self.sectionID,
            "noOfQns": self.noOfQns
        }