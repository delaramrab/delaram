def find_sum():
    sum_all = 0

    for number in range(123, 576):
        if number % 5 == 0 or number % 6 == 0:
            sum_all += number

    print(sum_all)


find_sum()