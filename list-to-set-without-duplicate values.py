#Convert a list to a set to remove duplicates

list_1 = [1,2,2,3,4,4,5,6,6,7]
print(f"Orignal list : {list_1}")
print()
l_s = set(list_1)
print(f"Converted List to Set: {l_s}")
final_list = list(l_s)
print()
print(f"Final List without Duplicate Values: {final_list}")

'''
Orignal list : [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

Converted List to Set: {1, 2, 3, 4, 5, 6, 7}

Final List without Duplicate Values: [1, 2, 3, 4, 5, 6, 7]
'''