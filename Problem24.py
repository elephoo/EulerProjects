# Lexicographic Permutations
from math import factorial

def nth_lexicographic_permutation(n,numbers):
    n -= 1
    numbers = sorted(numbers)
    nth_permutation = []
    for i in range(len(numbers) - 1, 0, -1):
        count = 0
        for j in range(i):
            if n - factorial(i) >= 0:
                count += 1
                n -= factorial(i)
            else:
                break
        nth_permutation.append(numbers[count])
        numbers.remove(numbers[count])
    nth_permutation += numbers
    return nth_permutation



numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nth_lexicographic_permutation(1000000, numbers_list))