class base1:
    def base_1(self):
        print("base 1")
class base2:
    def base_2(self):
        print("base 2")
class derived(base1,base2):
    def derived_class(self):
        print("derived from base1 and base2")
c=derived()
c.base_1()
c.base_2()
c.derived_class()