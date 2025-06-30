#Q3)Print all Armstrong numbers in a range.

def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    total = 0
    for d in digits:
        total += d ** power
    return total == num
def print_armstrong(start, end):
    print(f"Armstrong numbers between {start} and {end}:")
    for i in range(start, end + 1):
        if is_armstrong(i):
            print(i)
print_armstrong(1, 1000)
