# Tic Tac Toe by Harold Karibiye 
from random import randrange
import time
from copy import deepcopy
from tkinter import *
import tkinter.font as font 

#Create & Configure root 
root = Tk()
root.title("Tic Tac Toe")
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

#Create & Configure frame 
frame=Frame(root)
frame.grid(row=0, column=0, sticky=N+S+E+W)

#Create a 3X3 (rows x columns) grid of buttons inside the frame
def update_gui(board): #board):
    myFont = font.Font(family='Comic Sans MS', size=70, weight='bold')
    for row_index in range(3):
        Grid.rowconfigure(frame, row_index, weight=1)
        for col_index in range(3):
            Grid.columnconfigure(frame, col_index, weight=1)
            text_box = Text(frame, height=150, width=150)
            text_box['font'] = myFont
            text_box.tag_configure("center", justify='center')
            text_box.insert(INSERT, board[row_index][col_index])  # insert value
            text_box.tag_add("center", "1.0", "end")
            text_box.grid(row=row_index, column=col_index, sticky=N+S+E+W) 
     #size of the window
    root.geometry("400x400")
    root.update()

# gui displayed when the game is over 
def final_gui(board, chosen_list):
    myFont = font.Font(family='Comic Sans MS', size=70, weight='bold')
    for row_index in range(3):
        Grid.rowconfigure(frame, row_index, weight=1)
        for col_index in range(3):
            Grid.columnconfigure(frame, col_index, weight=1)
            if [row_index, col_index] in chosen_list:
                text_box = Text(frame, height=150, width=150, bg ='MediumOrchid4')
            else:
                text_box = Text(frame, height=150, width=150)
            text_box['font'] = myFont
            text_box.tag_configure("center", justify='center')
            text_box.insert(INSERT, board[row_index][col_index]) # insert value
            text_box.tag_add("center", "1.0", "end")
            text_box.grid(row=row_index, column=col_index, sticky=N+S+E+W) 
     #size of the window
    root.geometry("400x400")
    root.update()
    
# create board 
def create_board():
    board = [[' ' for j in range(3)] for i in range(3)]
    return board 

# print board 
def print_board(board):
    print('   ', end = '')
    for i in range(3):     
        print(str(i) + '   ' , end = '')
    print()
    print('-'* 15)

    for i in range(3):
        for j in range(3):
            if j == 0:
                print(str(i), end= '')
                print('|', end= '')
                print(' ' + board[i][j] + '  ', end= '' )

            elif j == 2:
                print(' ' + board[i][j] + ' ', end= '' )
                print('|', end= '')
                print(str(i))

            else:
                print(' ' + board[i][j] + ' ' , end =  ' ')
        if i != 2:
            print()
    print('-'* 15)

# def check_valid - check if play is valid no player there and in board 
def valid(x,y, board):
    # change to cover anything at all using try except 
    if type(x) != int or type(y) != int:
        print("Please enter integers for the co-ordinates")
        return False 
    if x >= 0 and x < 3:
        if y >= 0 and y < 3:
            if board[x][y] == ' ':
                return True
 
    print("Enter an empty position in the board")
    return False         

# get_move(p) gets coordinates from the command line 
def get_move(p):
    # modify to clicking on the gui 
    # return coordinates of onClick()? 
    x,y = input("Enter the co-ordinates of the desired position for " + p + " : ").split(',')
    return int(x), int(y)

def random_ai(p, board):
    # plays in random position 
    pos_x, pos_y = randrange(3), randrange(3)
    while board[pos_x][pos_y] != ' ':
        pos_x, pos_y = randrange(3), randrange(3)
    print()
    print("random_ai " + p + " playing...")
    print()   
    return pos_x, pos_y

def find_winning_moves_ai(p, board):
    # check for winning move and return the position
    # make a copy of the board
    # from copy import deepcopy
    faux_board = deepcopy(board) # list of list needs deep copy and list does not have this attribute 
    dict = {'X': 1,
            'O': 2 }
    for i in range(3):
        for j in range(3):
            if faux_board[i][j] == ' ':
                faux_board[i][j] = p
                if is_over(faux_board, dict[p]) == dict[p]:
                    print()
                    print("winning_moves_ai " + p + " playing...")
                    print()   
                    # print(i,j)
                    return i, j 
                else:
                    faux_board[i][j] = ' '

    # else play a random move 
    pos_x, pos_y = randrange(3), randrange(3)
    while board[pos_x][pos_y] != ' ':
        pos_x, pos_y = randrange(3), randrange(3)
    print()
    print("winning_moves_ai " + p + " playing...")
    print()   
    return pos_x, pos_y

def find_winning_and_losing_moves_ai(p, board):
    # find winning move if any
    faux_board = deepcopy(board) # list of list needs deep copy and list does not have this attribute 
    dict = {'X': 1,
            'O': 2 }
    for i in range(3):
        for j in range(3):
            if faux_board[i][j] == ' ':
                faux_board[i][j] = p
                if is_over(faux_board, dict[p]) == dict[p]:
                    print()
                    print("winning_and_losing_moves_ai " + p + " playing...")
                    print()   
                    # print(i,j)
                    faux_board[i][j] = ' ' # to ensure non tampered faux_board for loss check 
                    return i, j 
                else:
                    faux_board[i][j] = ' '

    # find if any a potential position for opponent win and play there 
    # note that this ai still loses if there are two ways 
    opp = {'X': 'O',
           'O': 'X'}
    val = opp[p]
    for i in range(3):
        for j in range(3):
            if faux_board[i][j] == ' ':
                faux_board[i][j] = val
                if is_over(faux_board, dict[val]) == dict[val]:
                    print()
                    print("winning_and_losing_moves_ai " + p + " playing...")
                    print()   
                    # print(i,j)
                    return i, j 
                else:
                    faux_board[i][j] = ' '

    # else play randomly 
    pos_x, pos_y = randrange(3), randrange(3)
    while board[pos_x][pos_y] != ' ':
        pos_x, pos_y = randrange(3), randrange(3)
    print()
    print("find_winning_and_losing_moves_ai " + p + " playing...")
    print()   
    return pos_x, pos_y

def get_legal_moves(board):
    # basically all free spots on the board 
    free = []
    for i in range(3):
        for j in range(3):
            if board[i][j] ==  ' ':
                free.append([i,j])
    return free    

# use dictionary to cache values to improve efficiency         
global dict_board 
dict_board = {}
def minmax_score(p, curr_p, board):
    global dict_board
    # if board in dictionary return the associated score 
    key = str(board)
    if key in dict_board:
        return dict_board[key]
    # If `board` is a terminal state, immediately
    # return the appropriate score.
    opp = {'X': 'O',
           'O': 'X'}
    p_opp = opp[p]

    dict = {'X': 1,
            'O': 2 }
    
    if is_over(board, dict[p]) == dict[p]: # p has won
        return +10
    elif is_over(board, dict[p_opp]) == dict[p_opp]: # p_opp has won
        return -10
    elif is_over(board, dict[p]) == 0: # draw
        return 0
    
    # If `board` is not a terminal state, get all
    # moves that could be played.
    legal_moves = get_legal_moves(board)

    # Iterate through these moves, calculating a score
    # for them and adding it to the `scores` array.
    scores = []
    for pos in legal_moves:
        # First make the move
        new_board = deepcopy(board)
        pos_x, pos_y = pos[0], pos[1]
        new_board[pos_x][pos_y] = curr_p 

        # Then get the minimax score for the resulting
        # state, passing in `current_player`'s opponents
        # because it's their turn now.
        curr_p_opp = opp[curr_p]
        score = minmax_score(p, curr_p_opp, new_board)
        scores.append(score)
    # we assume both our player and the opp would play optimally hence max for p
    # and min for p_opp as -10 means p_opp wins 
    if curr_p == p:
        value = max(scores)
        dict_board[key] = value
        return value
    else:
        value = min(scores)
        dict_board[key] = value
        return value

def minmax_ai(p, board):
    ''' 
    initialize dict {scores: [pos_x, pos_y]}
    initialize scores
    loop through the empty positions
    create temp_board and play in empty position. 
    score = minmax_score(p, curr_p, board)
    add score to scores 
    dict[score] = [i,j] # it's ok to change pos of same value scores 

    max_score = Math.max(scores)
    return dict[max_score][0], dict[max_score][1]

    '''
    opp = {'X': 'O',
           'O': 'X'}
    dict = {}
    scores = []
    temp_board = deepcopy(board)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                temp_board[i][j] = p
                # use opp[p] as p has played 
                score = minmax_score(p, opp[p], temp_board)
                scores.append(score)
                dict[score] = [i,j]
                temp_board[i][j] = ' '
    
    print()
    print("minmax_ai " + p + " playing...")
    print()   
    max_score = max(scores) # we are trying to maximize for p 
    return dict[max_score][0], dict[max_score][1] 
                 

def is_over(board, v, non_faux = False):
    chosen_list = []
    # v is either 1 or 2
    dict = {1: 'X',
            2: 'O' }
    # horizontal case
    for i in range(3):
        if board[i][0] == dict[v] and board[i][1] == dict[v] and board[i][2] == dict[v]:
            if non_faux == True:
                chosen_list.append([i,0])
                chosen_list.append([i,1])
                chosen_list.append([i,2])
                final_gui(board, chosen_list)
            return v
    # vertical case
    for j in range(3):
        if board[0][j] == dict[v] and board[1][j] == dict[v] and board[2][j] == dict[v]:
            if non_faux == True:
                chosen_list.append([0,j])
                chosen_list.append([1,j])
                chosen_list.append([2,j])
                final_gui(board, chosen_list)
            return v
    # diagonal case 
    if board[0][2] == dict[v] and board[1][1] == dict[v] and board[2][0] == dict[v]:
            if non_faux == True:
                chosen_list.append([0,2])
                chosen_list.append([1,1])
                chosen_list.append([2,0])
                final_gui(board, chosen_list)
            return v
    elif board[0][0] == dict[v] and board[1][1] == dict[v] and board[2][2] == dict[v]:
            if non_faux == True:    
                chosen_list.append([0,0]) 
                chosen_list.append([1,1])
                chosen_list.append([2,2])
                final_gui(board, chosen_list)
            return v
    # check for draw
    count = 0 
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O' or board[i][j] == 'X':
                count += 1
    if count == 9:  
        return 0
    # if game not over return -1
    return -1

def game():
    over = False 
    board = create_board()
    winner = []
    # print empty board 

    update_gui(board)
    while over != True:
        p1x, p1y = minmax_ai('X', board)# find_winning_and_losing_moves_ai('X', board) # get_move("X")
        while valid(p1x, p1y, board) != True:
            p1x, p1y = minmax_ai('x', board)# find_winning_moves_ai('X', board) # get_move("X")
        
        board[p1x][p1y] = "X"
        # delay for a few seconds before printing the board
        time.sleep(3)
        update_gui(board)
        # check if game over if it is change over to True 
        verdict = is_over(board, 1, non_faux = True)
        # print(verdict)
        if verdict != -1:
            winner.append(verdict)
            break 

        # repeat these for player 2
        p2x, p2y = find_winning_and_losing_moves_ai('O', board) # get_move("O")
        while valid(p2x, p2y, board) != True:
            p2x, p2y = find_winning_and_losing_moves_ai('O', board) # get_move("O")
        
        board[p2x][p2y] = "O"
        # delay for a few seconds before displaying the board
        time.sleep(3)
        update_gui(board)
        # check if game over if it is change over to True 
        verdict = is_over(board, 2, non_faux = True)
        if verdict != -1:
            winner.append(verdict)
            over = True

    return winner[0] # --> 0 for draw, 1 for p1, 2 for p2

# test game()
val = game()
if val == 1:
    print("The winner is X")
elif val == 2:
    print("The winner is O")
else: 
    print("Draw!") 
# loop until there is a win 
while val == 0:
    # don't do this for minmax_ai vs minmax_ai as neither will lose 
    val = game()
    if val == 1:
        print("The winner is X")
    elif val == 2:
        print("The winner is O")
    else: 
        print("Draw!") 


root.mainloop()

