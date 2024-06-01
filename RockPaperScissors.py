import random

choices = ['Rock', 'Paper', 'Scissors']
player_choice = ""
computer_choice = ""


def print_choices(player1, player2):
    print(f"You chose: {player1}. Computer chose: {player2}")


def play():
    player_choice: str = input('Enter your choice:')
    computer_choice = random.choice(choices)
    print_choices(player_choice, computer_choice)
    player_choice = player_choice.upper()
    computer_choice = computer_choice.upper()

    if player_choice == "" or computer_choice == "":
        print("Invalid game.")
    elif player_choice == computer_choice:
        print("Its a tie.")
    elif player_choice == "ROCK":
        if computer_choice == "PAPER":
            print("Paper covers Rock. You loose.")
        else:
            print("Rock smashes Scissors. You win.")
    elif player_choice == "PAPER":
        if computer_choice == "ROCK":
            print("Paper covers Rock. You win.")
        else:
            print("Scissors cut Paper. You loose")
    elif player_choice == "SCISSORS":
        if computer_choice == "ROCK":
            print("Rock smashes Scissors. You loose.")
        else:
            print("Scissors cut Paper. You win")


play()
