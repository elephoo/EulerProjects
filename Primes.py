from math import log


def upper_bound(n):
    return int(n * log(n) + n * log(log(n)) + 0.5)


def nth_prime(n):
    primes = primes_up_to(upper_bound(n))
    return primes[n - 1]

def primes_up_to(n):
    primes = []
    numbers = list(range(2, n + 1))
    for i in range(2, n + 1):
        if numbers[i - 2]:
            new_prime = numbers[i - 2]
            primes.append(new_prime)
            for j in range(i, n + 1, i):
                numbers[j - 2] = False
    return primes