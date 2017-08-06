def bank(start_count, years):
    res = start_count
    for i in range(years):
        res += res / 10
    print(res)


bank(12, 1)  # 13.2
bank(20, 2)  # 24.2
bank(50, 5)  # 80.5255
