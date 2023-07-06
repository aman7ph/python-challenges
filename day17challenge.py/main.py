from question_model import Question
from data import question_data
from quiz_brain  import QuizeBrain
question_bank=[]
for question in question_data:
    question_bank.append(Question(question['text'],question['answer']))

quize=QuizeBrain(question_bank)
loop=0
score=0
while loop<len(question_bank):
    quize.next_question()
    if quize.answer==question_bank[loop].answer:
        score+=1
        print("You got it right!")
        print(f"The correct answer was: {quize.answer}.")
        print(f"Your current score is: {score}/{loop+1}")
    else:
        print("That's wrong.")
        print(f"The correct answer was: {quize.answer}.")
        print(f"Your current score is: {score}/{loop+1}")
    loop+=1




