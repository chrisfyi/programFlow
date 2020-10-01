age = int(input("Enter your age: "))
name = input("Please enter your name: ")
holiday = 18 - 31

if age >= 18 <= 31:
    print("Welcome to the holiday, {}!".format(name))
else:
    print("Sorry, you are not invited")