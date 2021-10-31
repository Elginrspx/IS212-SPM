from os import set_inheritable
from main import db
from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKeyConstraint
from section import Section


class Score(db.Model):
    __tablename__ = 'scores'

    scoreStudentID = db.Column(db.String(30), primary_key=True)
    scoreCourseID = db.Column(db.String(30), primary_key=True)
    scoreClassID = db.Column(db.Integer, nullable=False)
    scoreSectionID = db.Column(db.String(30))
    scorePercentage = db.Column(db.String(30))
    attempts = db.Column(db.Integer)

    __table_args__ = (ForeignKeyConstraint([scoreCourseID, scoreClassID, scoreSectionID],
                                           [Section.secCourseID, Section.secClassID, Section.sectionID]),
                      {})
    sectionScore = db.relationship(
    'Section', primaryjoin='and_(Section.secClassID == Score.scoreClassID, Section.secCourseID == Score.scoreCourseID, Section.sectionID == Score.scoreSectionID)', backref='scores')

    def __init__(self, scoreStudentID, scoreCourseID, scoreClassID, scoreSectionID, scorePercentage, attempts):
        self.scoreStudentID = scoreStudentID
        self.scoreCourseID = scoreCourseID
        self.scoreClassID = scoreClassID
        self.scoreSectionID = scoreSectionID
        self.scorePercentage = scorePercentage
        self.attempts = attempts


    def json(self):
        return {
            "scoreStudentID" : self.scoreStudentID,
            "scoreCourseID" : self.scoreCourseID,
            "scoreClassID": self.scoreClassID,
            "scoreSectionID" : self.scoreSectionID,
            "scorePercentage": self.scorePercentage,
            "attempts": self.attempts
        }
    def create_score(studentID, courseID, classID, sectionID, score):
        try:
            studentScore = Score.query.filter_by(scoreStudentID=studentID, scoreCourseID=courseID, scoreClassID=classID, scoreSectionID=sectionID).first()
            studentScore.scorePercentage = score
            studentScore.attempts += 1
            db.session.commit()
            return 201, studentScore.json()
        # don't have existing
        except Exception as e:
            try:
                score = studentScore(studentID, courseID, classID, sectionID, score, 1)
                db.session.add(score)
                db.session.commit()
                return 201, score.json()
            except Exception as e:
                return 500, "Could not update score. " + str(e)

    def get_scores_for_sections(courseID, classID, sectionID):
        try:
            studentScore = db.session.query(Score.scoreStudentID, Score.scorePercentage, Score.attempts).filter(Score.scoreCourseID==courseID, Score.scoreClassID==classID, Score.scoreSectionID==sectionID).all()
            if studentScore:
                scoreList = []
                for scoreSet in studentScore:
                    scoreData = {}
                    scoreData["studentID"] = scoreSet[0]
                    scoreData["percentage"] = scoreSet[1]
                    if float(scoreSet[1]) > .8:
                        scoreData["status"] = "Pass"
                    else:
                        scoreData["status"] = "Fail"
                    scoreData["noAttempts"] = scoreSet[2]
                    scoreList.append(scoreData)
                    # print(scoreList)
                return 200, scoreList
        except Exception as e:
            return 404, "Could not get scores. " + str(e)

    def get_scores_by_student(data):
        courseID = data['courseID']
        classID = data['classID']
        sectionID = data['sectionID']
        studentID = data['studentID']
        try:
            studentScore = db.session.query(Score.scorePercentage).filter(Score.scoreCourseID==courseID, Score.scoreClassID==classID, Score.scoreSectionID==sectionID, Score.scoreStudentID == studentID).first()
            print(studentScore[0])

            return 200, studentScore[0]
        except Exception as e:
            return 404, "Could not get scores. " + str(e)



