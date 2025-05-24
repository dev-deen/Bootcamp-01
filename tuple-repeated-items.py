#Find the repeated items in a tuple

tup = (1,2,3,'T','T',30,30)
unique = set()
repeat = set()
for elements in tup:
    if elements in unique:
        repeat.add(i)
    else:
        unique.add(i)
print(f"Repeated iteam in tuple {tup} are {repeat}")
print(unique)

'''
Repeated iteam in tuple (1, 2, 3, 'T', 'T', 30, 30) are {'T', 30}
{1, 2, 3, 'T', 30}
'''