import math
def lcm(a, b):     #least common multiple
    return abs(a * b) // math.gcd(a, b)
print(lcm(6, 8))  
