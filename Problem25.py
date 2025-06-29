#1000-digit Fibonacci number
def smallest_fibonacci_above_n(n):
    last_values = (1,1)
    current_value = 0
    i = 2
    while current_value <= n:
        current_value = last_values[0] + last_values[1]
        last_values = (last_values[1],current_value)
        i += 1
    return i



print(smallest_fibonacci_above_n(10 ** 999))
