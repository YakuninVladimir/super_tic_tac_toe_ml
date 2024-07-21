class field_states:
    def __init__(self):
        self.value = ''
    
    def __str__(self):
        return self.value
    
    def running(self):
        self.value = 'running'

    def x_over(self):
        self.value = 'x wins'
    
    def o_over(self):
        self.value = 'x wins'