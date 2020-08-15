from tkinter import *
import tkinter.font as font 

#Create & Configure root 
root = Tk()
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
            text_box.insert(INSERT, board[row_index][col_index]) 
            text_box.tag_add("center", "1.0", "end")
            # text_box.tag_add("center", justify='center')
            text_box.grid(row=row_index, column=col_index, sticky=N+S+E+W) 
            
    # size of the window
    root.geometry("400x400")

    root.update()


            
# print(font.families())
#test game()
# val = game()
# print('The winner value is ' + str(val) ) 
# while val == 0:
#     # don't do this for minmax_ai vs minmax_ai 
#     val = game()
#     print('The winner value is ' + str(val) ) 
def create_board():
    board = [['O' for j in range(3)] for i in range(3)]
    return board 
board_x = create_board()

def create_boardx():
    board = [['X' for j in range(3)] for i in range(3)]
    return board 
board_y = create_boardx()
update_gui(board_y)
import time
time.sleep(4)
update_gui(board_x)

root.mainloop()

# # '''
# dict = dict(yes = 1 , no = 2)
# print(dict['yes'])
# # dict = {
# #     "yes": 1,
# #     "no": 2
# # }
# qa = 5
# print("yes {} {qa}".format("yessir", qa = qa))
# print("hhdh " + str(2))

# print("dict values are {yes} and {no}".format(**dict))
# from math import pi
# from string import ascii_lowercase
# from collections import defaultdict
# print(ascii_lowercase)
# if 'a' in ascii_lowercase:
#     print(True)

# print("bdshhs " + str(qa) + " yesssir. \n weee wbwuwu")