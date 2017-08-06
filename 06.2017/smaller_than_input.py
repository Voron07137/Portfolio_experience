def smaller_than_five(list):
    return [item for item in list if item < 5]


def smaller_than_input(list, input):
    return [item for item in list if item < input]


arr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(smaller_than_five(arr))  # [1, 1, 2, 3]
print(smaller_than_input(arr, 15))  # [1, 1, 2, 3, 5, 8, 13]
