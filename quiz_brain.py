class QuizBrain:
    def __init__(self, input):
        self.question_number = 0
        self.question_list = input
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer != correct_answer:
            print("wrong answer")
        else:
            self.score += 1
            print("correct")
        print(f"the answer is {correct_answer}")
        print(f"your current score is {self.score}/{self.question_number}")
        print("\n")

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}. {question.text} (True/False): ")
        self.check_answer(user_answer.lower(), question.answer.lower())

    def get_score(self):
        return self.score

    def get_num_of_questions(self):
        return len(self.question_list)



