from art_and_data import day7challenge_word
from art_and_data import day7challenge_Art
import random

logo=day7challenge_Art.logo
Art=day7challenge_Art.stages
words=day7challenge_word.word_list

print(logo)


randindex=random.randint(0,len(words)-1)
new_word=words[randindex].lower()
print(new_word)

end_game=False

input_char=input('\n \n Guess a letter: \t').lower()


length_of_new_word=len(new_word)

store=[]


count=0
while not end_game:
    #print(input_char)
    if input_char in new_word:

        if input_char in store:
             print(f"You've already guessed {input_char}")
             new_input_char=input('\n \n Guess a letter: 1\t').lower()
             input_char=new_input_char          
             
        else:
            print('you gase correct')
            store.append(input_char)
            new_input_char=input('\n \n Guess a letter: 2\t').lower()
            input_char=new_input_char
            
            if len(store)==length_of_new_word:
                end_game = True
     
    else:
        count+=1
        if count==length_of_new_word:
            print("You lose.")
            end_game = True
        else:
            print(f"You guessed {input_char}, that's not in the word. You lose a life.")
            new_input_char=input('\n \n Guess a letter: 3\t').lower()
            input_char=new_input_char

    
        

    
    


