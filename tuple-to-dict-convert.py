#Convert a tuple to a dictionary

tup = (1,2,3,[4,5],'six',"seven",9.11,True)
tup1 = dict(enumerate(tup))
print(tup)
print()
print(tup1)

'''
(1, 2, 3, [4, 5], 'six', 'seven', 9.11, True)

{0: 1, 1: 2, 2: 3, 3: [4, 5], 4: 'six', 5: 'seven', 6: 9.11, 7: True}

'''