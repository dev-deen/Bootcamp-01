d={'a':[1,2,2],'b':[2,3,3]}
dup={k:list(set(v))for k,v in d.items()}
print(dup)