def is_prime(n):
    for i in range(2,n+1):
        if n % i == 0:
            return False
        return True
print(is_prime(4))
