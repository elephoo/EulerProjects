def power_digit_sum(n, power):
    x = str(n ** power)
    total = 0
    for i in x:
        total += int(i)
    return total

print(power_digit_sum(2, 1000))