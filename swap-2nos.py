#Swap two variables without using a temporary variable
x = int(input("Enter first num: ))
y = int(input("Enter second num: "))
print("Before Swap - x is ", x, " and y is ", y)
x , y = y , x
print("After Swap - x is ", x, " and y is ", y)