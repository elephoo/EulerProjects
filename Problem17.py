def letters_of_ones(n):
    letters = ""
    match n:
        case 0:
            letters = ""
        case 1:
            letters = "one"
        case 2:
            letters = "two"
        case 3:
            letters = "three"
        case 4:
            letters = "four"
        case 5:
            letters = "five"
        case 6:
            letters = "six"
        case 7:
            letters = "seven"
        case 8:
            letters = "eight"
        case 9:
            letters = "nine"
    return letters



def letters_of_tens(n):
    tens = (n // 10) % 10
    ones = n % 10
    letters = ""
    if tens == 1:
        match ones:
            case 0:
                letters = "ten"
            case 1:
                letters = "eleven"
            case 2:
                letters = "twelve"
            case 3:
                letters = "thirteen"
            case 4:
                letters = "fourteen"
            case 5:
                letters = "fifteen"
            case 6:
                letters = "sixteen"
            case 7:
                letters = "seventeen"
            case 8:
                letters = "eighteen"
            case 9:
                letters = "nineteen"
    else:
        match tens:
            case 2:
                letters = "twenty"
            case 3:
                letters = "thirty"
            case 4:
                letters = "forty"
            case 5:
                letters = "fifty"
            case 6:
                letters = "sixty"
            case 7:
                letters = "seventy"
            case 8:
                letters = "eighty"
            case 9:
                letters = "ninety"
            case _:
                letters = ""
        letters += letters_of_ones(ones)
    return letters



def letters_of_hundreds(n):
    letters = ""
    hundreds = (n // 100) % 10
    tens = n % 100
    letters = letters_of_ones(hundreds)
    if hundreds:
        letters += "hundred"
    if hundreds and tens:
        letters += "and"
    letters += letters_of_tens(tens)
    return letters



total = 0
for x in range(1, 1000):
    total += len(letters_of_hundreds(x))
total += len("onethousand")
print(total)