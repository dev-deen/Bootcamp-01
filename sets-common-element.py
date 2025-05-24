#Find common elements between two sets

set_x = {1,2,3,4,5,0}
set_y = {3,4,5,6,7,8,9,0}
common_element = set_x.intersection(set_y)
print(f"common element {common_element}")

'''
common element {0, 3, 4, 5}
'''