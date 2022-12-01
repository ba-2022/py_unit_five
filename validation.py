

def get_input():

    while True:
        get_number = input("Enter a number between 1 and 10")

        if int(get_number) >=1 and int(get_number) <= 10:
            return get_number



def main():
    print(get_input())



main()
