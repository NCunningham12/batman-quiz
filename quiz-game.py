
questions = [
  {
    "prompt": "What is Batman's real name?",
    "options": ["A. Clark Kent", "B. Dick Grayson", "C. Bruce Wayne", "D. None of the Above"],
    "answer": "C"
  },
  {
    "prompt": "Which one of these is NOT one of Batman's gadgets?",
    "options": ["A. Shrink Ray", "B. Grapnel Gun", "C. Batarang", "D. Explosive Gel"],
    "answer": "A"
  },
  {
    "prompt": "Which of these is NOT a batman villian?",
    "options": ["A. Joker", "B. CandleJack", "C. Mad Hatter", "D. Deathstroke"],
    "answer": "B"
  },
  {
    "prompt": "Which movie has the best Batmobile?",
    "options": ["A. Batman 1989", "B. The Batman (2022)", "C. The Dark Knight", "D. None of the Above"],
    "answer": "B"
  }
]

def run_quiz(questions):
  score = 0
  for question in questions:
    print(question["prompt"])
    for option in question["options"]:
      print(option)
    user_answer = input("\nEnter Your Answer \n\n")

    if user_answer == question["answer"]:
      score += 1
      print("Correct!!!, your score is now " + str(score) + "! \n\n")
    else:
      print("Sorry, not quite. The answer was actually " + question["answer"] + ". \n\n")

  print("Your Final Score is " + str(score) + "/4 correct!")

run_quiz(questions)
