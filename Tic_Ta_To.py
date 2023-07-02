import os


board=[""," "," "," "," "," "," "," "," "," "]
love=True
hermi=True
player2_mark=""

def display_board(board):
    os.system('cls')   
  
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
 
    print('-----------')
  
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])

    print('-----------')

    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

def checkX(board):
    global hermi
    if board[7]==board[8]==board[9]=='X':
        print("player with 'X' mark is a winer") 
        boot=False             
    elif board[4]==board[5]==board[6]=='X': 
        print("player with 'X' mark is a winer")
        boot=False           
    elif board[1]==board[2]==board[3]=='X': 
        print("player with 'X' mark is a winer")
        boot=False             
    elif board[1]==board[5]==board[9]=='X':
        print("player with 'X' mark is a winer") 
        boot=False           
    elif board[3]==board[5]==board[7]=='X': 
        print("player with 'X' mark is a winer") 
        boot=False

def checkO(board):
    global hermi
    if board[7]==board[8]==board[9]=='O':
        print("player with 'X' mark is a winer")
        hermi=False               
    elif board[4]==board[5]==board[6]=='O': 
        print("player with 'X' mark is a winer")
        hermi=False             
    elif board[1]==board[2]==board[3]=='O': 
        print("player with 'X' mark is a winer")
        hermi=False              
    elif board[1]==board[5]==board[9]=='O':
        print("player with 'X' mark is a winer")
        hermi=False             
    elif board[3]==board[5]==board[7]=='O': 
        print("player with 'X' mark is a winer")
        hermi=False  


while love:
    player1_mark=input("you are player 1 wich marker do you want 'X' or 'O' ").upper()
    if player1_mark=='X':
        player2_mark='O'
    else:
        player2_mark='X'
    
    while hermi:
        board_position = int(input("Player 1 Please enter a number for the board position choice(1-9): "))
        board[board_position]=player1_mark
        display_board(board)

        if player1_mark=='X':
            checkX(board)
        else:
            checkO(board)
        
        board_position = int(input("Player 2  Please enter a number for the board position choice(1-9): "))
        board[board_position]=player2_mark
        display_board(board)

        if player2_mark=='O':
            checkO(board)
        else:
            checkX(board)

    cont=input("do you want to contniu playing Yes('Y') or No('N'): ").lower()
    if cont=='y':
        love=True
        hermi=True
        board=[""," "," "," "," "," "," "," "," "," "]
        os.system('cls') 
    else:
        break



    
    
    








 

 
        






