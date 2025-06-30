#Q5)Convert decimal to binary, octal, and hexadecimal.

def convert(n, base):
    digits = "0123456789ABCDEF"
    res = ""
    while n > 0:
        res = digits[n % base] + res
        n //= base
    return res or "0"
num = 45
print("Decimal:", num)
print("Binary:", convert(num, 2))
print("Octal:", convert(num, 8))
print("Hexadecimal:", convert(num, 16))
