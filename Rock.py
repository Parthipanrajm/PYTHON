import random

def get_choice():
    player_choice = input( "please enter ur choice 1 2 3:" )
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choice = {"player": player_choice, "computer": computer_choice}
    return choice

def check_win(player, computer):
  ##print( "you chose: " + player + " computer chose: " + computer )
  print( f"you chose: {player}, computer chose: {computer}" )
  if player == computer:
    return "It is  tie"
  elif player == "rock":
    if computer == "scissors":
       return "Rock smashes scis YOU WIN!"
    else:
       return "Paper cover Rock YOU LOSE!!"
  elif player == "paper":
    if computer == "rock":
       return "Paper cover Rock  YOU WIN!"
    else:
       return "Scissors cut paper YOU LOSE!!"
  elif player == "Scissors":
    if computer == "paper":
       return "Scissors cut paper  YOU WIN!"
    else:
       return "Rock smashes scis  YOU LOSE!!"

choices = get_choice()
result = check_win(choices["player"], choices["computer"])
print(result)





