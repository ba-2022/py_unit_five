def sequence(number):
    """
    If the number n is odd - 3*n + 1
    If the number n is even n / 2
    :param number: The starting number for the Hailstone sequence
    :return: The number of steps taken to reach 1
    """
number = input("Enter number")
    while True:
        if number % 2== 0:
            number = number / 2
            counter = counter + 1
            if number == 1:
                return counter

        if number % 2== 1:
            number = number *  3 + 1
            counter = counter + 1
            if number == 1:
                return counter


def main():
    sequence(number)

main()