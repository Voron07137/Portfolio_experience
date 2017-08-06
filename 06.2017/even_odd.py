def even_odd_user_processing(num, check):
    str_num = str(num)
    if num % 2 == 0:
        print("The number " + str_num + " is even!")
        if num % 4 == 0:
            print("The number " + str_num + " is a multiple of 4!")
    else:
        print("The number " + str_num + " is odd!")

    str_check = str(check)
    str_remainder = str(num % check)

    if str_remainder == 0:
        print("The number " + str_num + " is divided by " + str_check + " without remainder!\n")
    else:
        print("The number " + str_num + " is divided by " + str_check + " with remainder " + str_remainder + "!\n")


even_odd_user_processing(8, 3)  # even, mult of 4, remainder 2
even_odd_user_processing(25, 5)  # odd, remainder 0
even_odd_user_processing(34, 7)  # even, remainder 6
even_odd_user_processing(91, 13)  # odd, remainder 0
even_odd_user_processing(7, 5)  # odd, remainder 2
