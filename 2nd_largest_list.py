a=[]
n=int(input("enter number of element:"))
for i in range(1,n+1):
 b=int(input("enter element :"))
 a.append(b)
a.sort()
print("second largest no. :",a[n-2])