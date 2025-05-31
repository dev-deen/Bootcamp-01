def factors(n):
    factors=set()
    for i in range(1,n+1):
        if n % i == 0:
            factors.add(i)
    return factors
    
def gcd(x,y):
    factors_x=factors(x)
    factors_y=factors(y)
    common=factors_x.intersection(factors_y)
    return (max(common))

print(gcd(12,18))