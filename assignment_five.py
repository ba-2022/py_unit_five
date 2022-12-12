#Betelhem Alemu
#12/7/22
#Guessing Game
import random


for x in range(3):
    def get_number():
        number = random.randint(1,100)
        print(number)


    def get_guess(counter):
        number = get_number()
        while True:
            guess = int(input("enter your guess"))
            counter += 1
            if guess == number:
                print("You guessed correctly!")
                break

            if guess > number:
                print("That's too high, guess lower")
            if guess < number:
                print("That's too low, guess higher")


def main():
    counter = 0
    get_number()
    get_guess(counter)
    print(counter)



main()