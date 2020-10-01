low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1
while low != high:
    # print("\tGuessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter H or L or C if my guess is correct. "
                     .format(guess)).casefold()

    if high_low == "h":
        #  Guess higher. The low end of the range becomes
        #  1 greater than the guess.
        low = guess + 1
    elif high_low == "l":
        #  Guess Lower. The high end of the range becomes
        #  one less than the guess.
        high = guess - 1
    elif high_low == "c":
        #  The guess is correct
        print("I got it in {} guesses!".format(guesses))
        break  # when the program hits this break point it hits the else
        # and prints the strings on 35/36
    else:
        print("Please enter h, l or c")

    # guesses = guesses + 1
    guesses += 1  # this is shorthand for line 28

else:
    print("You thought of the number {}.".format(low))
    print("I got it in {} guesses".format(guesses))

