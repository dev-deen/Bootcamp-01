#Q6)Calculate the sum of digits of a number.

def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
num = 1234
print("Sum of digits:", sum_of_digits(num))
