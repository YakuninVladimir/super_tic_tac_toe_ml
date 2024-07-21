import numpy as np 
import pandas as pd
from states import field_states

class cell:
    
    def __init__(self):
        self.s_field = np.ndarray(2, 2).fill(0)
        self.game_state = field_states().running()

class field:
    pass

    def __init__(self):
        pass

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass

