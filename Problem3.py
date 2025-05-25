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

if __name__ == '__main__':
    print(prime_factors(600851475143))