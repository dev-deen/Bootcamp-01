tup=(1,2,3,4,4)
repeated=set([item for item in tup if tup.count(item)>1])
print(repeated)