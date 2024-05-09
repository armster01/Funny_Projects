import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissor): ")
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You choose {player}, computer choose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "Scissor":
            return "Rock smashes scissor! You Win!!"
        else:
            return "Paper covers rock! You Loose!!"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You Win!!"
        else:
            return "Scissor cuts paper! You Loose!!"
    elif  player == "scissor":
        if computer == "paper":
            return "Scissor cuts paper! You Win!!"
        else:
            return "Rock smashes scissor! You Loose!!"
        
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)