def rock_scissors_paper(player_one_answer, player_two_answer):
    guns = ["rock", "scissors", "paper"]
    if player_one_answer == player_two_answer:
        return "Draw"
    elif (player_one_answer == guns[0] and player_two_answer == guns[1]) or \
            (player_one_answer == guns[1] and player_two_answer == guns[2]) or \
            (player_one_answer == guns[2] and player_two_answer == guns[0]):
        return "Player 1 is Winner!"
    elif (player_two_answer == guns[0] and player_one_answer == guns[1]) or \
            (player_two_answer == guns[1] and player_one_answer == guns[2]) or \
            (player_two_answer == guns[2] and player_one_answer == guns[0]):
        return "Player 2 is Winner!"
    else:
        return "Wrong input!"


def input_answers():
    print("Input first player's answer")
    first_answer = input()
    print("Input second player's answer")
    second_answer = input()
    print(rock_scissors_paper(first_answer, second_answer))


while True:
    print("Play rock_scissors_paper? Yes or No")
    user_answer = input()
    if user_answer == "No":
        break
    elif user_answer == "Yes":
        input_answers()
    else:
        print("Wrong answer!")
