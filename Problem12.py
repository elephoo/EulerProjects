from Primes import prime_factors
from math import prod
from collections import Counter

def number_of_factors(n):
    counted = Counter(prime_factors(n))
    added_numbers = [x+1 for x in counted.values()]
    return prod(added_numbers)

def triangle_factors(n):
    triangle_number = 0
    for x in range(1, 10**10):
        triangle_number += x
        if number_of_factors(triangle_number) > n:
            return triangle_number
    return None

print(triangle_factors(500))