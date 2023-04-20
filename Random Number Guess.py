import random

class Invalid_Command(Exception):
    pass


print("Guess the hidden number which is between 1 and 100.")
print("There are 2 types of game mode: easy(with clues) and hard(without clues).")
print("You can change the mode you want to play anytime.")
guessed_number = "Congratulations! You guessed the number!"
print("Type play to start the game or stop to stop the game")


def play_easy():
    hidden_number = random.choice([i for i in range(100)])
    while True:
        number = int(input("Type your guess:"))
        if number < hidden_number:
            print(f"The number is higher than {number}.")
        elif number > hidden_number:
            print(f"The number is lower than {number}.")
        else:
            print(guessed_number)
            break


def play_hard():
    hidden_number = random.choice([i for i in range(100)])
    while True:
        number = int(input("Type your guess:"))
        if number == hidden_number:
            print(guessed_number)
            break


def play(mode):
    if mode == "easy":
        play_easy()
    elif mode == "hard":
        play_hard()


while True:
    command = input()
    if command == "play":
        mode = input("Choose your mode: easy or hard: ")
        play(mode)
    elif command == "stop":
        break
    else:
        raise Invalid_Command("Invalid command! The valid ones are 'play' and 'stop'!")



