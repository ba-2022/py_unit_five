
'''
def get_sum(number):
    sum = 0
    for x in range(number):
        if x % 3 == 0 or x % 5 == 0:
            sum += x
    print("The sum of the multiples of 3 and 5 up to", number - 1, "is", sum)

get_sum(11)

'''

'''
x = 0
while x < 5:
    print(x)
    x = x + 1
'''

'''
while true: 
    play_again = input("play again (y/n):")
    if play_again == "y" or play_again == "n":
        break 
 '''

import random

tries = 0
total = 0

while total != 12:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    tries += 1
    total = die1 + die2

print("It took", tries, "tries to get a 12")
