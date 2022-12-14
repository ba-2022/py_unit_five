#Betelhem Alemu
#12/14/22
#Guessing Game
import random

'''
This function allows the computer to generate a random number between 1 and 100, and then returns the number

'''
def get_number():
    number = random.randint(1,100)
    print("Computers number is", number)
    return number

'''
This function allows the user to guess the number and when they do it tells them if they are correct,
and if they are it tells them how many tries it took them. If they are not correct, it tells them whether the 
guess was too low or too high
'''

def get_guess(counter, number):
        while True:
            guess = int(input("enter your guess"))
            counter += 1                                                     # keeps track of the number of guesses
            if guess == number:
                print("You guessed correctly! It took you", counter, "tries")
                break                                                       # if user is correct, it breaks the while true and asks again

            if guess > number:
                print("That's too high, guess lower")
            if guess < number:
                print("That's too low, guess higher")

def main():
    for x in range(3):
        counter = 0
        computer_number = get_number()
        get_guess(counter, computer_number)
        print(counter)
    print("Thanks for playing!")


main()