d={'a':2,'b':1,'c':3}
sort=dict(sorted(d.items(),key=lambda item: item[1]))
print(sort)