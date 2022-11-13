#Betelhem Alemu
#11/10/22

def count(first, last, m):
    test = ""
    for x in range(first, last, m):
        test += str(x)+ " "
    print(test)

def main():

    (count(0, 7, 1))
    (count(6, -1, -1))


main()
