def remainder(d):
    remainders = set()
    n = 1
    length = 0
    while True:
        if n % d not in remainders:
            if n >= d:
                remainders.add(n % d)
                n = n % d
            n *= 10
            length += 1
        else:
            return length



longest_decimal_length = 0
longest_divisor = 0
for d in range(1, 1000):
    if remainder(d) > longest_decimal_length:
        longest_decimal_length = remainder(d)
        longest_divisor = d


print(longest_divisor)