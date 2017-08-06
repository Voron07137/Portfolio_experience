import uuid
import random


def password_generator(length):
    password = str(uuid.uuid4())
    password = password.replace("-", "")
    password = password[0:length]
    password_elems = list(password)
    result_elems = []
    for item in password_elems:
        random_zero = random.randint(0, 1)
        if random_zero == 1:
            result_elems.append(item.upper())
        else:
            result_elems.append(item)
    return "".join(result_elems[::])


print(password_generator(20))
print(password_generator(14))
print(password_generator(17))
print(password_generator(25))
print(password_generator(30))
