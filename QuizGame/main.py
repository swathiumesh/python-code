from typing import Any

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data :
    QuestionObject = Question ( question [ "text" ] , question [ "answer" ] )
    question_bank.append ( QuestionObject )
    # print ( question_bank )

qb = QuizBrain(question_bank)
while qb.still_has_question():
    qb.next_question()