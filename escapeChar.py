split_string = "This string has been\nsplit over\nseveral\nlines"
print(split_string)

tabbed_string = "1\t2\t3\t4\t5"
print(tabbed_string)

print('The pet shop owner said "No, no, \'e\'s uh,... he\'s resting".')
#or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")
#or
print("""The pet shop owner said "No, no, 'e's uh,... he's resting".""")

another_split_string = """This string has been \
                        split over \
                        several \
                        lines"""

print(another_split_string)

# print("C:\Users\chrisfyi\notes.txt") \U \n are uses for escape chars
# and need to be escaped
print("C:\\Users\\chrisfyi\\notes.txt")
# or
print(r"C:\Users\chrisfyi\notes.txt")