import random 

options = ("rock", "paper", "scissor")
player = None 
computer  = random.choice(options)

player = input("Enter a choice (rock, paper, scissor):")

print(f"Player: {player}")
print(f"Computer: {computer}")

if player == computer:
    print("Its a tie!")

elif player == "rock" and computer == "scissor":
    print("You win!")

elif player == "scissor" and  computer == "paper":
    print("Your win!")

elif player =="scissor" and computer == "rock":
    print("You lose!")

elif player == "paper" and computer == "rock":
    print("You win!")

else:
    print("You lose!")

print("Thanks for playing!")