#Write a function to calculate compound interest

def compound_i(p, r, n, t):
    return p * (1 + r / n) ** (n * t)
    
print(compound_i(1000, 25, 1, 1))