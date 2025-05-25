def collatz_sequence(n):
    x = 0
    while n !=  1:
        if not n % 2:
            n /= 2
        else:
            n = (n * 3) + 1
        x += 1
    return x

def colltz_highest_chain(n):
    highest_chain = 0
    highest_chain_start = 0
    for i in range(1, n):
        current_sequence = collatz_sequence(i)
        if current_sequence > highest_chain:
            highest_chain = current_sequence
            highest_chain_start = i
    return highest_chain_start

print(colltz_highest_chain(1000000))