from math import log


def upper_bound(n):
    return int(n * log(n) + n * log(log(n)) + 0.5)


def nth_prime(n):
    primes = primes_up_to_n(upper_bound(n))
    return primes[n - 1]

def primes_up_to_n(n):
    primes = []
    numbers = list(range(2, n + 1))
    for i in range(2, n + 1):
        if numbers[i - 2]:
            new_prime = numbers[i - 2]
            primes.append(new_prime)
            for j in range(i, n + 1, i):
                numbers[j - 2] = False
    return primes


def prime_factors(number):
    factors = []
    current_factor = 2
    while number % current_factor == 0:
        factors.append(current_factor)
        number /= current_factor
    current_factor += 1
    while number != 1:
        if number % current_factor == 0:
            factors.append(current_factor)
            number /= current_factor
        else:
            current_factor += 2
    return factors
