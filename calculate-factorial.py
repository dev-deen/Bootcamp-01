#Write a function to calculate factorial of a number

def fact(n):
    factorial = 1
    
    for num in range(1,n+1):
        factorial = factorial * num
        print(f"{num}'s factororial = {factorial}")
        
print(fact(5))