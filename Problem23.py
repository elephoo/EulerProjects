from Problem21 import factors

def is_abundant(n):
    if sum(factors(n)) > n:
        return True
    else:
        return False



def abundance_below_n(n):
# Starts at 12 because 12 is the smallest abundant number.
    return [x for x in range(12, n + 1) if is_abundant(x)]



def find_abundant_sums(abundant_list):
    abundant_sums = set()
    for i, x in enumerate(abundant_list):
        for y in abundant_list[i:]:
            abundant_sums.add(x + y)
    return abundant_sums



def non_abundant_sums_below_n(n):
    numbers_below_n = {x for x in range(n)}
    return numbers_below_n - find_abundant_sums(abundance_below_n(n))


print(sum(non_abundant_sums_below_n(28123)))