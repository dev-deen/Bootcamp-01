#Perform union, intersection, and difference on two sets

set_1 = {1,2,3,4,5,6,7,8}
set_2 = {6,7,8,9,0}
u = set_1 | set_2
i = set_1 & set_2
d = set_1.difference(set_2)  #Removes all same values of self set and 
sd = set_1.symmetric_difference(set_2)
print("Union", u)
print("Intersection", i)
print("Difference", d)
print("Symmetric Difference", sd)

#Symmetric_difference - Returns elements that are in either A or B, but not in both
#difference - Returns elements that are in A but not in B

'''
Union {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
Intersection {8, 6, 7}
Difference {1, 2, 3, 4, 5}
Symmetric Difference {0, 1, 2, 3, 4, 5, 9}
'''