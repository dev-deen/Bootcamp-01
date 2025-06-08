def gcd(a, b):      #Gretest common divisor
    while b != 0:
        a, b = b, a % b
    return a
print(gcd(48, 18))  
