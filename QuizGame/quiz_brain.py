class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        num = self.question_number
        usr_ans = input(f"Q.{num} {current_question.text} (True/False): ")
        self.check_answer(usr_ans, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You are right")
        else:
            print("You are wrong")
        print(f"Correct Answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{len(self.question_list)}")
