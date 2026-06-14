import random 

lowest_num = 1 
highest_num = 100

answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True 

print("Python number guessing game")
print(f"Select a number between {lowest_num} to {highest_num}")

while is_running:
    guess = input("Enter your guess:")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1 

        if guess<lowest_num or guess>highest_num:
            print("That number is out of range!")
            print(f"Please select a number between {lowest_num} to {highest_num}")

        elif guess<answer:
            print("Too low. Try again!!")

        elif guess>answer:
            print("Too high. Try again!!")

        else:
            print(f"Correct! The answer is {answer}")
            print(f"Number of guesses: {guesses}")
            
    else:
        print("Invalid guess!")
        print(f"Please select a number between {lowest_num} to {highest_num}")