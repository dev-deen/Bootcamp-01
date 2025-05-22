# without importing
mylist=[1,2,3,4,5]
mul=1
for i in mylist:
    mul*=i
print("product:",mul)

# with import
import math
mylist=[1,2,3,4,5]
product=math.prod(mylist)
print("product:",product)