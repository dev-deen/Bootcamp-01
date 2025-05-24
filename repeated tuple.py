tuple=(2,3,4,55,55,65)
repeated_element= set([item for item in tuple if tuple.count(item)>1])
print(repeated_element)