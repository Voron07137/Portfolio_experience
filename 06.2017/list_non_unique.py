def delete_unique(list_int):
    result_list = []
    for item in list_int:
        if list_int.count(item) > 1:
            result_list.append(item)
    return result_list


def search_min(list_int):
    if not list_int:
        return None
    else:
        res = list_int[0]  # first element
        for item in list_int:
            if item < res:
                res = item
        return res


def output_min(list_int):
    if search_min(list_int) is None:
        print("Empty list!")
    else:
        print(search_min(list_int))


c = [1, 2, 3, 1, 3]  # [1, 3, 1, 3]
print(delete_unique(c))
c = [1, 2, 3, 4, 5]  # []
print(delete_unique(c))
c = [5, 5, 5, 5, 5]  # [5, 5, 5, 5, 5]
print(delete_unique(c))
c = [10, 9, 10, 10, 9, 8]  # [10, 9, 10, 10, 9]
print(delete_unique(c), '\n')

c = [1, 2, 3, 4, 5]  # 1
output_min(c)
c = [12, 21, 4, -3, 1]  # -3
output_min(c)
c = [322, 321, 54, 32, 7]  # 7
output_min(c)
c = [-5, 27, -43, 9, 90]  # -43
output_min(c)
c = []  # Empty list!
output_min(c)
