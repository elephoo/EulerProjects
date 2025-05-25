def pythagorean_triple(a,b,c):
        return a**2 + b**2 == c**2

for a in range(1,250):
    for b in range(a + 1,499):
        for c in range(b + 1, 1000 - (a + b)):
            if pythagorean_triple(a,b,c):
                print(a,b,c)