def is_palindrome(num):
    return str(num) == str(num)[::-1]


largest_palindrome = 0
for i in range(999,100,-1):
    if i * 999 < largest_palindrome:
        break
    for j in range(999,100,-1):
        if is_palindrome(i * j):
            if i * j > largest_palindrome:
                largest_palindrome = i * j
                break


print(largest_palindrome)