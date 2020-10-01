choice = "-"  # Use a variable that wont be used so that choice is
#               defined but it wont run anything in the code

while choice != "0":  # while the choice is not equal to 0, if the
    #  input is in the string then, print. Else choose from the list.
    if choice in "12345":
        print("You chose {}".format(choice))

    else:
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")

    choice = input()
