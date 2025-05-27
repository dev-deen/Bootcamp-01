my_dict={'a':[1,1,2],'b':[3,3,4]}
no_dup={k:list(set(v)) for k, v in my_dict.items()}
print(no_dup)