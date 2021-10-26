from main import db
from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKeyConstraint


class Score(db.Model):
    __tablename__ = 'scores'

    scoreStudentID = db.Column(db.Integer, primary_key=True)
    scoreCourseID = db.Column(db.Integer, primary_key=True)
    scoreClassID = db.Column(db.String(30), nullable=False)
    scoreSectionID = db.Column(db.String(30))
    scorePercentage = db.Column(db.Integer)


    def __init__(self, scoreStudentID, scoreCourseID, scoreClassID, scoreSectionID, scorePercentage):
        self.scoreStudentID = scoreStudentID
        self.scoreCourseID = scoreCourseID
        self.secClassID = scoreClassID
        self.scoreSectionID = scoreSectionID
        self.scorePercentage = scorePercentage


    def json(self):
        return {
            "scoreStudentID" : self.scoreStudentID,
            "scoreCourseID" : self.scoreCourseID,
            "scoreClassID": self.scoreClassID,
            "scoreSectionID" : self.scoreSectionID,
            "scorePercentage": self.scorePercentage
        }
    def create_score(studentID, courseID, classID, sectionID, score):
        try:
            studentScore = Score.query.filter_by(scoreStudentID=studentID, scoreCourseID=courseID, scoreClassID=classID, scoreSectionID=sectionID).first()
            studentScore.scorePercentage = score
            db.session.commit()
            return 201, studentScore.json()
        # don't have existing
        except Exception as e:
            try:
                score = studentScore(studentID, courseID, classID, sectionID, score)
                db.session.add(score)
                db.session.commit()
                return 201, score.json()
            except Exception as e:
                return 500, "Could not update score. " + str(e)

    def get_scores_for_sections(studentID, courseID, classID, sectionID, score):
        return 

