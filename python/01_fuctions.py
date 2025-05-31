def factorial_function(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
        print(i,factorial)
print(factorial_function(4))