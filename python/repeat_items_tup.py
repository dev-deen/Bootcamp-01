tup=(1,2,3,4,2,1,2,)
repeated=[]
for x in tup:
    if tup.count(x)>1 and x not in repeated:
        repeated.append(x)
        print("repeated items:",repeated)
   