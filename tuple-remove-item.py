#Remove an item from a tuple

tup = (1,2,3,4,5)
print(f"Orignal tuple {tup}")
tup_list = list(tup)
print(f"List of Tuple {tup_list}")
r = tup_list.remove(3)
list_tup = tuple(tup_list)
print(f"Orignal tuple after remove {list_tup}")

'''
Orignal tuple (1, 2, 3, 4, 5)
List of Tuple [1, 2, 3, 4, 5]
Orignal tuple after remove (1, 2, 4, 5)
'''