rows = int(input("Enter the rows"))

for i in range(1, rows + 1):
    for j in range(rows - i):
        print("", end = '')

    for x in range(i):
        print("#", end = ' ')

    print()


