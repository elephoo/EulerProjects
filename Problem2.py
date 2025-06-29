def fibonacci_up_to_n(n):
    last_values = (0,1)
    current_value = 0
    while current_value <= n:
        current_value = last_values[0] + last_values[1]
        last_values = (last_values[1],current_value)
        if current_value <= n:
            yield current_value

total = 0
for value in fibonacci_up_to_n(4000000):
    if value % 2 == 0:
        total += value

print(total)