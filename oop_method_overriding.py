class A :
    def greet(self):
        print("Hello c++!")
class B(A):
    def greet(self):
        print("Hello python!")
p = A()
p.greet()  
c = B()
c.greet()  