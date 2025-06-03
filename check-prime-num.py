#Write a function to check if a number is prime

def prime(n):
    for num in range(2,n-1):
        if n % num == 0:
            return False
        
    return True
            
print(prime(18))            