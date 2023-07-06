class QuizeBrain:
    def __init__(self,question_bank):
        self.question_number=0
        self.question_list=question_bank
        self.answer=""

    def next_question(self):
            self.answer=input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].question}. (True/False):").lower()
            self.question_number+=1
            



""" QuizeBra=QuizeBrain()
QuizeBra.next_question() """