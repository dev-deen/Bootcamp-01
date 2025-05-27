tup=(1,2,3,4,5,6)
item_to_rem=2
tup=tuple(x for x in tup if x != item_to_rem)
print(tup)