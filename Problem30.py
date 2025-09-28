#Digit Fifth powers

def digit_power_sum(power):
    return sum(n for n in range(2 ** power, (9 ** power) * len(str(9 ** power))) if n == sum(int(digit) ** power for digit in str(n)))

print(digit_power_sum(5))

