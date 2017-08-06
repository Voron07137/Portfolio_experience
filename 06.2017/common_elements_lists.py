import random


def random_list(length):
    list = []
    for item in range(0, length):
        list.append(random.randint(0, 100))
    return list


def common_elements_list(list1, list2):
    return [item for item in list1 if item in list2]


def output_common_elements(list1, list2):
    if len(list1) == len(list2):
        print("Lists have the same length!")
    else:
        print("list1: " + str(list1))
        print("list2: " + str(list2))
        print(common_elements_list(list1, list2), "\n")


output_common_elements(random_list(5), random_list(8))
output_common_elements(random_list(20), random_list(15))
output_common_elements(random_list(10), random_list(10))
