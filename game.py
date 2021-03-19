# User name
user_name = input("Enter your name:")
print(f"Hello, {user_name}")
# Use score starting point
file_name = open("rating.txt")
for file_n in file_name:
    names, scores = file_n.split()
    if user_name == names:
        score = int(scores)
file_name.close()

# Rules for game start
options_input = input()
if not options_input:
    options = ["rock", "paper", "scissors"]
else:
    options = options_input.split(",")
print("Okay, let's start")
# Start game !
from random import choice
computer_choice = choice(options)
while True:
    user_input = input()
    if user_input in options:
        chosen_index = options.index(user_input)
        new_options = options[chosen_index + 1: :] + options[0:chosen_index]
        win_list = new_options[0:(len(new_options) // 2)]
        lose_list = new_options[(len(new_options) // 2): :]
        if user_input == computer_choice:
            print(f"There is a draw {computer_choice}")
            score += 50
        elif user_input not in new_options and computer_choice in win_list:
            print(f"Sorry, but the computer chose {computer_choice}")
        elif user_input not in new_options and computer_choice in lose_list:
            print(f"Well done. The computer chose {computer_choice} and failed")
            score += 100
    elif user_input == "!exit":
        print("Bye!")
        break
    elif user_input == "!rating":
        print(f"Your rating: {score}")
    else:
        print("Invalid input")
    computer_choice = choice(options)
