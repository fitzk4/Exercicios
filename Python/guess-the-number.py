import random

number = random.randint(1,10)
play = True


while play:
    guess = int(input('Guess a number from 1 to 10: '))

    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    elif guess == number:
        print("You win!")
        break
