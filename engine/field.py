import numpy as np 
import pandas as pd

#states for small field
from states import field_st

# 3x3 field
class small_field:
    def __init__(self):
        # print('meow')
        #initialise cells of small field

        #0 -- cell is empty
        #1 -- cell contains X
        #2 -- cell contains O

        self.s_field = np.ndarray((3, 3), dtype='int8')
        self.s_field.fill(0)
    

        #game has several states:
        #running(0), x_won(1), y_won(2), draw(3)

        self.game_state = field_st.running
    
    #calculate, what is the state of game (somebodies win, draw, or game is still running)
    def evaluate_state(self):
        #if game has ended before state can't change, so we need to check only if game is running 
        if self.game_state == field_st.running:
            #check triple of X or O in rows
            for row in range(3):
                if self.s_field[row, 0] == self.s_field[row, 1] == self.s_field[row, 2] != 0:
                    return field_st(self.s_field[row, 1])
            #check triple of X or O in columns 
            for col in range(3):
                if self.s_field[0, col] == self.s_field[1, col] == self.s_field[2, col] != 0:
                    return field_st(self.s_field[1, col])
            #check triple of X or O in diagonals 
            if self.s_field[0, 0] == self.s_field[1, 1] == self.s_field[2, 2] != 0:
                return field_st(self.s_field[1, 1])
            if self.s_field[0, 2] == self.s_field[1, 1] == self.s_field[0, 2] != 0:
                return field_st(self.s_field[1, 1])
            
            #check for draw
            void_flag = False
            for i in np.nditer(self.s_field):
                if i == 0:
                    void_flag = True
                    break
            
            if not void_flag:
                return field_st.draw
        return self.game_state
    
    def __getitem__(self, key):
        return self.s_field[key]

    def __setitem__(self, key, value):
        cases = {"X" : 1, "O" : 2}
        self.s_field[key] = cases[value]

    
    #converts one row of field to string
    def line_to_str(self, ind):
        line = self.s_field[ind, :]
        def el_str(arr, ind):
            cases = {0 : " ", 1 : "X", 2 : "O"}
            return cases[arr[ind]]
        return f"{el_str(line, 0)}|{el_str(line, 1)}|{el_str(line, 2)}"

    #method for printing small field
    def __str__(self):
        res_str = "-----\n"

        for i in range(3):
            res_str += self.line_to_str(i)
            res_str += "\n-----\n"
        
        return res_str


#main field
class large_field:
    def __init__(self):
        self.cells = np.array([[small_field() for j in range(3)] for i in range(3)])
        
        
    #getter and setter for items of main field
    def __getitem__(self, key):
        return self.cells[key]

    def __setitem__(self, key, value):
        self.cells[key] = value

    #method for printing main field
    def __str__ (self):
        res_str = "-" * (8 + 5*3) + "\n"
        for i in range(3):
            # print(self.cells)
            line = self.cells[i, :]
            for j in range(3):
                res_str += "||" + line[0].line_to_str(j) + "||" + line[1].line_to_str(j) + "||" + line[2].line_to_str(j) + "||" + "\n" 
            res_str += "-" * (8 + 5*3) + "\n"
        return res_str            