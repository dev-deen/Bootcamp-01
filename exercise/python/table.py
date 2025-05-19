no=int(input("Enter a number:"))
if no>0:
  print("Table of ",no)
  for i in range(1,11):
    print(no,"*",i,"=",no*i)
else:
  print("Number not valid")
