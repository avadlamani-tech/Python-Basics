rows = int(input("Enter the rows"))
for i in range(rows, 0, -1):
    for j in range(i):
        print(i,end = ' ')
    print()