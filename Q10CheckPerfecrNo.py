#Q10)Check if a number is perfect number.

def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n
num = 28
if is_perfect(num):
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")
