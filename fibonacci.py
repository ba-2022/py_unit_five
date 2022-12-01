
'''

param: number
'''

def fibonacci(number):
    a = 1
    b = 1

    listOfNumbers = "1 1"
    for x in range(7):
        c = a + b
        listOfNumbers += str(c) + "  "
        a = b
        b = c
    print(listOfNumbers)

fibonacci(12)