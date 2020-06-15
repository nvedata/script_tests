class Bar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.c = x * y
        
    def calc(self):
        return self.c ** 0.5 - self.x
    
    @classmethod    
    def load(cls, attr_dict):
        b = object.__new__(cls)
        for k, v in attr_dict.items():
            setattr(b, k, v)
        return b
        
b = Bar.load({'x' : 1, 'y' : 2, 'c' : 2})
b.calc()
