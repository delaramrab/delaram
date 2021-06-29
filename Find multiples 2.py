def find(number: int):
    print(number)


for num in range(200, 20, -1):
    if num % 3 != 0 and num % 5 == 0:
        find(num)
    else:
        continue
