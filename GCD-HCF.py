#Write a function to find GCD of two numbers

def factors(n):
    factors = set()
    
    for i in range(1,n+1):
        if n%i == 0:
            factors.add(i)
    return factors
print(factors(21))
print(factors(24))

def gcd(x, y):
    factors_x = factors(x)
    factors_y = factors(y)
    
    c_factors = factors_x.intersection(factors_y)
    return max(c_factors)
print()
print(gcd(21,24))