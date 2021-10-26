from main import db
from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKeyConstraint
from section import Section


class Question(db.Model):
    __tablename__ = 'questions'

    qnCourseID = db.Column(db.String(30), primary_key=True)
    qnClassID = db.Column(db.Integer, nullable=False, primary_key=True)
    qnSectionID = db.Column(db.String(30), nullable=False, primary_key=True)
    question = db.Column(db.String(255), primary_key=True)
    answer = db.Column(db.String(255), nullable=False)
    choices = db.Column(db.String(255), nullable=False)

    __table_args__ = (ForeignKeyConstraint([qnCourseID, qnClassID, qnSectionID],
                    [Section.secCourseID, Section.secClassID, Section.sectionID]),
                      {})
    sectionQuiz = db.relationship(
    'Section', primaryjoin='and_(Question.qnClassID == Section.secClassID, Section.secCourseID == Question.qnCourseID, Section.sectionID == Question.qnSectionID)', backref='questions')

    def __init__(self, qnCourseID, qnClassID, qnSectionID, question, answer, choices):
        self.qnCourseID = qnCourseID
        self.qnClassID = qnClassID
        self.qnSectionID = qnSectionID
        self.question = question
        self.answer = answer
        self.choices = choices


    def json(self):
        return {
            "qnCourseID" : self.qnCourseID,
            "qnClassID": self.qnClassID,
            "qnSectionID" : self.qnSectionID,
            "question": self.question,
            "answer": self.answer,
            "choices": self.choices
        }

    def get_questions(qnCourseID, qnClassID, qnSectionID):
        print("hiiii")
        
        try:
            questions = db.session.query(Question.question, Question.answer, Question.choices).filter(qnCourseID==Question.qnCourseID, qnClassID == Question.qnClassID, qnSectionID == Question.qnSectionID).all()
            if questions:
                questionList = []
                for questionSet in questions:
                    questionData = {}
                    questionData["question"] = questionSet[0]
                    questionData["answer"] = questionSet[1]
                    questionData["choices"] = questionSet[2]
                    questionList.append(questionData)
                return 200, questionList
        except Exception as e:
            return 404, "Questions not available" + str(e)

