import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


def player_shape():
    p1=""
    while p1.upper() not in ["X","O"]:
        p1=input("Hey Player 1 please chose you shape X or O: ")
    if p1.upper() == 'O':
        p2="X"
    elif p1.upper() =="X":
        p2="O"
    print("Player 1 Shape: {} \n"
          "Player 2 Shape: {} ".format(p1,p2))
    return p1.upper(),p2


def print_board(board_list):

    print("\n"*15)
    line="---------"
    print(board_list[7], "|", board_list[8], "|", board_list[9])
    print(line)
    print(board_list[4],"|", board_list[5],"|", board_list[6])
    print(line)
    print(board_list[1], "|", board_list[2], "|", board_list[3])

"""
def player_input(board_list):

    in_p1=""
    r=False
   
    while not in_p1.isdigit() and not r:
        in_p1=input("Chose location: ")
    
    int(in_p1)
    
    while not in_p1>0 and not in_p1<10:
        while not in_p1.isdigit():
            in_p1 = input("Chose location: ")
        int(in_p1)
    
    if

"""

def place_marker(board, marker, position):
    board[position]=marker
"""
def win_check1(board, mark):
    windic ={"row":[[1,2,3],[4,5,6],[7,8,9]],
              "column":[[3,6,9],[2,5,8],[1,4,7]],
              "cross":[[1,5,9],[3,5,7]]}
    b1=False
    b2 = False
    b3 = False
    
    for win in windic:#row /column / cross
        for i in windic[win]: #list of chekes [1,2,3],[4,5,6],[7,8,9] i = small list
            if b1==False or b2==False or b3==False: #
                b1 = False
                b2 = False
                b3 = False
            for j in i:
                if mark ==board[j]:
                    
                else:
                    break
    return r==3

"""


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def space_check(board, position):
    """Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available."""
    return board[position]==" "

def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')





print('Welcome to Tic Tac Toe!')

while True:
#Set the game up here
    board_list = [' '] * 10
    print_board(board_list)
    p1,p2=player_shape()

    while not full_board_check(board_list):
        # Player 1 Turn
        position1=player_choice(board_list)
        place_marker(board_list,p1,position1)
        print_board(board_list)
        if win_check(board_list,p1):
            print('Player1 win!!!!')
            break
        # Player2's turn.
        position2 = player_choice(board_list)
        place_marker(board_list, p2, position2)
        print_board(board_list)
        if win_check(board_list,p2):
            print('Player2 win!!!')
            break

    if not replay():
        break

print_board(board_list)

