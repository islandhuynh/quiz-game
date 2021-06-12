from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
  question_bank.append(Question(question["text"], question["answer"]))
quiz = QuizBrain(question_bank)
while (quiz.question_number < len(question_bank)):
  quiz.next_question()
print(f"Your final score is {quiz.score}/{len(question_bank)}.")