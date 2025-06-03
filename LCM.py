#Write a function to calculate LCM of two numbers

def factors(n):
    factors = set()
    
    for i in range(2,n+1):
        if n%i == 0:
            factors.add(i)
    return factors
print(factors(12))
print(factors(16))

def lcm(x, y):
    factors_x = factors(x)
    factors_y = factors(y)
    
    c_factors = factors_x.intersection(factors_y)
    return min(c_factors)
print()
print(lcm(12,16))