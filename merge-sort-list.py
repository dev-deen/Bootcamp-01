#Merge two lists and sort them

l1 = [1,9,2,8,3,0]
l2 = [4,6,7,5,3]
merge = l1 + l2
s = sorted(merge)
print(f"Orignal List : {l1} and {l2}")
print(f"Merged List : {merge}")
print(f"Sorted List : {s}")