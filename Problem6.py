def square_of_sum(num):
    result = sum(x ** 3 for x in range(1, num + 1))
    return result

def sum_of_squares(num):
    result = sum(x ** 2 for x in range(1, num + 1))
    return result


print(square_of_sum(100) - sum_of_squares(100))