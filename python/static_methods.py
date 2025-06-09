class myclass:
    count=0
    def __init__(self):
        myclass.count += 1
    @classmethod
    def show(cls):
        print("count:",cls.count)

    @staticmethod
    def greet():
        print("hello!")
s=myclass
myclass.show()
myclass.greet()