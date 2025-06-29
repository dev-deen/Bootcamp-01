class me:
    def show_me(self):
        print("This is my class")
class friend:
    def show_friend(self):
        print("This is friend class")
class friend2(me, friend):
    def show_friend2(self):
        print("This is friend2 class")
c = friend2()
c.show_me()
c.show_friend()
c.show_friend2()