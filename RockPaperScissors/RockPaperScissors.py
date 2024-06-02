import random
from Action import Action

choices = [f"{action.name}[{action.value}]" for action in Action]
choices_str = ",".join(choices)

victories = {
    Action.Rock: [Action.Scissors, Action.Lizard],
    Action.Paper: [Action.Rock, Action.Spock],
    Action.Scissors: [Action.Paper, Action.Lizard],
    Action.Lizard: [Action.Spock, Action.Paper],
    Action.Spock: [Action.Scissors, Action.Rock]
}

def get_user_choice():
    choice = int(input(f"Enter your choice {choices_str}:"))
    return Action(choice)

def get_computer_choice():
    return Action(random.randint(0, len(Action)-1))

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        print(f"Both chose {player_choice.name}. Its a tie.")
    else:
        defeats = victories[player_choice]
        if computer_choice in defeats:
            print(f"{user_choice.name} beats {computer_choice.name}! You Win!")
        else:
            print(f"{computer_choice.name} beats {user_choice.name}! You loose!")


while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    determine_winner(user_choice, computer_choice)
    choice = input("Continue y/n?")
    if choice.lower() != "y":
        break
