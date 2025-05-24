#Check if a set is a subset of another set

set_x = {1,2,3,4,5}
set_y = {1,2,3,9,0}
sub_set = set_x.issubset(set_y)
print(sub_set)


set_a = {1,2,3,4,5}
set_b = {1,2,3,4,5,6,7,8,9,0}
sub_set = set_a.issubset(set_b)
print(sub_set)

'''
False
True
'''