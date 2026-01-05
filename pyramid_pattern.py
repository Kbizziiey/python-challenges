row = 5

i = 1

while i <= row:
    j = 1
    while j <= row - i:
        print(" ", end="")
        j += 1

    j = 1
    while j <= 2 * i - 1:
        print("*", end="")
        j += 1

    print()
    i += 1