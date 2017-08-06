import random

attempts = 0
while True:
    if attempts == 0:
        number = random.randint(1, 9)
    print('Enter an integer from 1 to 9 (Input "Exit" to escape)')
    user_attempt = input()
    if user_attempt == "Exit":
        break
    else:
        int_input = int(user_attempt)
        if 1 <= int_input <= 9:
            attempts += 1
            if int_input == number:
                print("Exactly right! Attempts: " + str(attempts) + "\n")
                attempts = 0
            elif int_input < number:
                print("Too low!")
            else:
                print("Too high!")
        else:
            print("Wrong input!")
