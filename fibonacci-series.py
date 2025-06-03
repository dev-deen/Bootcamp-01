#Write a function to generate Fibonacci sequence up to n terms
def fib(n):
    arr = []
    for num in range(0,n+1):
        if num == 0:
            arr.append(0)
        elif num == 1:
            arr.append(1)
        else:
            arr.append(arr[num-1] + arr[num-2])
            print(arr)
print(fib(6))