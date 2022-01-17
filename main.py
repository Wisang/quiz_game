from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for _ in question_data:
    question_bank.append(Question(_["question"], _["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"Game over. Your final score is {quiz.get_score()}/{quiz.get_num_of_questions()}")
