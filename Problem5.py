from collections import defaultdict

from Problem3 import prime_factors

factors = defaultdict(int)
for i in range(2,20):
    current_factors =  prime_factors(i)
    for j in current_factors:
        if current_factors.count(j) > factors[j]:
            factors[j] = current_factors.count(j)


products = [x**y for x,y in factors.items()]
total = 1
for i in products:
    total *= i
print(total)