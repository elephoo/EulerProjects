def sum_multiples(number):
    total = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


print(sum_multiples(1000))
