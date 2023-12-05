""" Get the number of prime numbers in given range, and this use Sieve of Eratosthenes algo
"""
from math import sqrt

def get_primes(n: int) -> int:
    if n <=2:
        return 0
    primes = [1]*n
    primes[0] = primes[1] = 0

    for i in range(2, n//2+1):
        if primes[i]:
            # from i square to n fill all with 0 that are divisible by i as 
            # using i in step and this is Sieve of Eratosthenes.
            primes[i*i:n:i] = [0]* len(primes[i*i:n:i])
    # summing as we only have primes with 1
    return sum(primes)

def get_primes_navie(n: int):
    if n <=2:
        return 0
    elif n ==3:
            return 1
    c = 2
    # here time complexity is O(n)
    for i in range(4, n):
        is_prime = True
        for j in range(2, i//2+1):
            if not i%j:
                is_prime = False
                break
        if is_prime:
            print(i)
            c+=1
    return c


if __name__ == "__main__":
    assert get_primes(10) == 4

    assert get_primes(0) == 0
    
    assert get_primes(1) == 0

    # assert get_primes(-1991) == False