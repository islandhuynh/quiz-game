class QuizBrain:
  def __init__(self, q_list):
      self.question_number = 0
      self.question_list = q_list
      self.score = 0

  def next_question(self):
    user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].question} (True/ False)?: ")
    if user_answer == self.question_list[self.question_number].answer:
      self.score += 1
      print("You got it right!")
      print(f"The correct answer was: {self.question_list[self.question_number].answer}.")
      print(f"Your current socre is: {self.score}/{self.question_number + 1}.")
    else:
      print("That's wrong.")
      print(f"Your current socre is: {self.score}/{self.question_number + 1}.")
    print("\n")

    self.question_number += 1
