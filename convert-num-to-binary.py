#Write a function to convert a number to binary

def convert(num):
    
    binary = ''
    while (num != 0):
        r = num % 2
        q = num // 2
        binary = str(r) + binary
        num = q
    return binary
    
print(convert(3095))