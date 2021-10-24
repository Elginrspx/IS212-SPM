from main import db


class Question(db.Model):
    __tablename__ = 'questions'

    secCourseID = db.Column(db.Integer, primary_key=True)
    secClassID = db.Column(db.String(30), nullable=False)
    sectionID = db.Column(db.String(30))
    question = db.Column(db.String(255))
    answer = db.Column(db.String(255))
    other = db.Column(db.String(255))


    def __init__(self, secCourseID, secClassID, sectionID, question, answer, other):
        self.secCourseID = secCourseID
        self.secClassID = secClassID
        self.sectionID = sectionID
        self.question = question
        self.answer = answer
        self.other = other


    def json(self):
        return {
            "secCourseID" : self.secCourseID,
            "secClassID": self.secClassID,
            "sectionID" : self.sectionID,
            "question": self.question,
            "answer": self.answer,
            "other": self.other
        }