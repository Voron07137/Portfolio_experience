def is_prime(number):
    res = True
    if number == 0 or number == 1:
        res = False
    else:
        for item in range(2, number // 2 + 1):
            if number % item == 0:
                res = False
                break
    return res


def output_prime(number):
    number_str = str(number)
    if is_prime(number) is False:
        print(number_str + " is composite!")
    else:
        print(number_str + " is prime!")


output_prime(0)  # composite
output_prime(1)  # composite
output_prime(2)  # prime
output_prime(5)  # prime
output_prime(12)  # composite
output_prime(23)  # prime
output_prime(35)  # composite
output_prime(47)  # prime
output_prime(91)  # composite
output_prime(101)  # prime
