class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number].text
        correct_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}. {current_question}(True/False): ")
        self.check_answer(user_answer, correct_answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        # if self.question_number < len(self.question_list):
        #     return True
        # return False

    def check_answer(self, user_answer, correct_answer):
        if correct_answer.lower() == user_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
            print(f"The right answer : {correct_answer} ")
        print(f"Your current score : {self.score}/{self.question_number}")




