import numpy as np 
import pandas as pd
from states import field_states




# Часть поля, представляющая из себя 3x3 ячейки
class hashtag_field_part:
    def __init__(self):
        # ВНИМАНИЕ: тип ячейки - int8
        # -1 == X
        # 1 == O
        # 0 == neutral

        self.s_hashtag = np.zeros((3,3), np.int8)
        self.field_state = "neutral"
    def state(self):
        if self.field_state == "O_won":
            return "O_won"
        elif self.field_state == "X_won":
            return "X_won"
        elif self.field_state == "neutral":
            h = self.s_hashtag
            # По строкам
            for i in range(2):
                if h[i][0] == h[i][1] and h[i][1] == h[i][2]:
                    if h[i][0] == -1:
                        self.field_state == "X_won"
                        return "X_won"
                    elif h[i][0] == 1:
                        self.field_state == "O_won"
                        return "O_won"
            # По столбцам
            for i in range(2):
                if h[0][i] == h[1][i] and h[1][i] == h[2][i]:
                    if h[0][i] == -1:
                        self.field_state == "X_won"
                        return "X_won"
                    if h[0][i] == 1:
                        self.field_state == "O_won"
                        return "O_won"
            if h[0][0] == h[1][1] and h[1][1] == h[2][2]:
                if h[0][0] == -1:
                    self.field_state == "X_won"
                    return "X_won"
                if h[0][0] == 1:
                    self.field_state == "O_won"
                    return "O_won"
            if h[0][2] == h[1][1] and h[1][1] == h[2][1]:
                if h[0][2] == -1:
                    self.field_state == "X_won"
                    return "X_won"
                if h[0][2] == 1:
                    self.field_state == "O_won"
                    return "O_won"
            return "neutral"
        else:
            print("ERROR: wrong hashtag state format")



# Поле, представляющее из себя 3*3 field_part
class field:
    pass

    def __init__(self):
        pass

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass

