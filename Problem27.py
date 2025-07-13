#Quadratic primes
from Primes import primes_up_to_n


def quadratic_primes(n):
    highest_count = 0
    highest_coefficients = 0
    primes = primes_up_to_n(n ** 2)
    n_primes = primes_up_to_n(n)
    for a in range(-n + 1, n, 2):
        for b in n_primes:
            count = 0
            for x in range(n):
                if (x**2 + a*x + b) in primes:
                    count += 1
                else:
                    if count > highest_count:
                        highest_count = count
                        highest_coefficients = (a, b)
                    break
    return highest_coefficients, highest_count


print(quadratic_primes(1000))