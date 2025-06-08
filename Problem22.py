with open('0022_names.txt', 'r') as file:
    names = file.read()


def alphabetical_value(word):
    return sum(ord(char) - 64 for char in word)

names = names.replace("\"", "")
names_list = names.split(',')
names_list = sorted(names_list)


def list_value(list_of_strings):
    total = 0
    for i, word in enumerate(list_of_strings):
        total += alphabetical_value(word) * (i + 1)
    return total


print(list_value(names_list))