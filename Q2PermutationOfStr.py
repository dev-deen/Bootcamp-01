#Q2)Find all permutations of a string.
from itertools import permutations
s = "abc"
perm = permutations(s)
for p in perm:
    print(''.join(p))
