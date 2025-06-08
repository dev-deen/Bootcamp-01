class Num:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        return Num(self.val + other.val)
    def __mul__(self, other):
        return Num(self.val * other.val)
    def show(self):
        print(self.val)
a = Num(2)
b = Num(3)
c = a + b
d = a * b
c.show()  
d.show()  
