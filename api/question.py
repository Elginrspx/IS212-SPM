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
    isMultiple = db.Column(db.String(5), nullable=False)

    __table_args__ = (ForeignKeyConstraint([qnCourseID, qnClassID, qnSectionID],
                    [Section.secCourseID, Section.secClassID, Section.sectionID]),
                      {})
    sectionQuiz = db.relationship(
    'Section', primaryjoin='and_(Question.qnClassID == Section.secClassID, Section.secCourseID == Question.qnCourseID, Section.sectionID == Question.qnSectionID)', backref='questions')

    def __init__(self, qnCourseID, qnClassID, qnSectionID, question, answer, choices, isMultiple):
        self.qnCourseID = qnCourseID
        self.qnClassID = qnClassID
        self.qnSectionID = qnSectionID
        self.question = question
        self.answer = answer
        self.choices = choices
        self.isMultiple = isMultiple


    def json(self):
        return {
            "qnCourseID" : self.qnCourseID,
            "qnClassID": self.qnClassID,
            "qnSectionID" : self.qnSectionID,
            "question": self.question,
            "answer": self.answer,
            "choices": self.choices,
            "isMultiple": self.isMultiple
        }

    def get_questions(qnCourseID, qnClassID, qnSectionID):
        try:
            questions = db.session.query(Question.question, Question.choices, Question.isMultiple, Question.answer).filter(qnCourseID==Question.qnCourseID, qnClassID == Question.qnClassID, qnSectionID == Question.qnSectionID).all()
            if questions:
                questionList = []
                for questionSet in questions:
                    questionData = {}
                    questionData["answer"] = questionSet[3]
                    questionData["question"] = questionSet[0]
                    questionData["choices"] = questionSet[1]
                    questionData["isMultiple"] = questionSet[2]
                    questionList.append(questionData)
                return 200, questionList
        except Exception as e:
            return 404, "Questions not available" + str(e)


    def compute_score(data, qnCourseID, qnClassID, qnSectionID):
        maxscore = len(data)
        score = 0
        answerKey = db.session.query(Question.question, Question.answer).filter(qnCourseID==Question.qnCourseID, qnClassID == Question.qnClassID, qnSectionID == Question.qnSectionID).all()
        for qn1 in data:
            for qn2 in answerKey:
                if qn1["qn"] == qn2[0]:
                    if qn1["ans"] == qn2[1]:
                        score += 1
                        break
        score_percentage = score/maxscore
        return score_percentage

        

    def create_question(data):
        data = data['data']
        data2 = data[0]
        try:
            check = Question.query.filter_by(qnCourseID = data2['qnCourseID'], qnClassID =data2['qnClassID'], qnSectionID = data2['qnSectionID']).all()
            for entries in check:
                db.session.delete(entries)
            db.session.commit()
        except Exception as e:
            print("Could not delete qns. "+ str(e))
        # print(data)
        for qn in data:
            question = Question(qn["qnCourseID"], qn["qnClassID"], qn["qnSectionID"], qn["question"], qn["answer"], qn["choices"], qn["isMultiple"])
            db.session.add(question)
        db.session.commit()
        return 201, len(data)

        

