def multiplication_table(number):

    test = ""
    for x in range(13):
        test += str(x * number)+ " "
    print(test)

def main():

    (multiplication_table(6))

#
#
main()
