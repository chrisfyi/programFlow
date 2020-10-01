# day = "Friday"
# temperature = 30
# raining = False
#
# if (day == "Saturday" and temperature > 27) or not raining:
#     print("Go swimming")
# else:
#     print("Learn Python")

#zero is evaluated as false in a boolean expression
if 0:
    print("True")
else:
    print("False")

print("-----------")

#an empty string is also evaluated as false in a boolean
name = input("Enter your name: ")
# if name:
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")


