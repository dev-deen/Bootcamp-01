#Q7)Find all prime numbers in a range (Sieve of Eratosthenes).

def primes(n):
    p = [1] * (n + 1)
    p[0] = p[1] = 0
    for i in range(2, n + 1):
        if p[i]:
            for j in range(i * 2, n + 1, i):
                p[j] = 0
    for i in range(n + 1):
        if p[i]:
            print(i, end=' ')
primes(30)
