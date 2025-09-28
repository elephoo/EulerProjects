#Distinct Powers

def distinct_powers(n):
    return len(set(a ** b for a in range(2, n + 1) for b in range(2, n + 1)))


print(distinct_powers(100))