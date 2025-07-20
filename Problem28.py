def spiral_diagonals(n):
    total = 1
    current_number = 1
    second_difference = 2
    count = 0
    for i in range(n // 2 * 4):
        current_number += second_difference
        total += current_number
        count = (count + 1) % 4
        if count == 0:
            second_difference += 2
    return total



print(spiral_diagonals(1001))