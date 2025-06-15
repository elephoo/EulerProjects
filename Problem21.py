from itertools import count

from Primes import prime_factors
from collections import Counter



def p_factors_to_divisors(primes_count, possible_factors):
    # recursively determine the proper factors
    # stopping criteria: if we are at the end, return the possible factors
    if not primes_count:
        return possible_factors

    prime, count = primes_count[0]

    # update the possibilities to the possible factors list
    updated_possibilities= []
    for factor in possible_factors:
        for i in range(count + 1):
            updated_possibilities.append(factor * prime ** i)

    # recursively return: call with the remainder of the prime_counts and the possibility list
    return p_factors_to_divisors(primes_count[1:], updated_possibilities)



def factors(n):
    return p_factors_to_divisors(list(Counter(prime_factors(n)).items()), [1])[:-1]



def amicable(a):
    if a == 1:
        return False
    b = sum(factors(a))
    if sum(factors(b)) == a and a != b:
        return True
    else:
        return False



if __name__ == '__main__':



    total = 0
    for x in range(1, 10000):
        if amicable(x):
            total += x

    print(total)