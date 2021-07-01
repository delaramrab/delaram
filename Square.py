height = int(input("Please insert the value of height: "))
length = int(input("Please insert the value of length: "))

for row in range(height, 0, -1):
    print(' ' * (row - 1), end="")

    for column in range(length):

        if row == 1 or row == height or column == 0 or column == length - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()
