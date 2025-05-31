def fibonacci_series(n):
    array=[]

    for i in range(0,n+1):
        if i==0:
            array.append(0)
        elif i==1:
            array.append(1)
        else:
            array.append(array[i-1] + array[i-2])
            print(array) 
print(fibonacci_series(6))   