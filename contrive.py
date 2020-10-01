numbers = [1, 45, 31, 12, 60]

for number in numbers:
    if number % 8 == 0:
        # reject the list
        print("The numbers are unacceptable")
        break
else:
    print("All those numbers are fine")
# In this example the for loop runs the if statement and if its true it
# breaks out of the loop, If its not it moves on to else.