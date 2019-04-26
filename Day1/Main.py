def math(number1, number2, choice):
    switcher = {
        '1': number1 + number2,
        '2': number1 - number2,
        '3': number1 * number2,
        '4': number1 / number2,
    }
    return switcher.get(choice, "nothing")



name = input('Enter your name: ')
introduction = "Hello "
wellcome = " wellcome to Calculator"
if len(name) > 0 and name.isalpha():
    output = introduction + name + wellcome
    print(output)
else:
    print("Invialid name")
while (input('To continue enter something, to exit press enter: ')):
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    # Get the math choice from the user
    choice = input("Enter your choice 1/2/3/4: ")
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    result = math(n1, n2, choice)
    if (result != "nothing"):
         print (result)
    else:
        print ("invalid math case")


