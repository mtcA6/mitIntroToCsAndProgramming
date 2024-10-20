# Finger Exercise Lecture 2
# Assume you are given a variable named number (has a numerical value). Write a piece of Python code that prints out
# one of the following strings:
#
# positive if the variable number is positive
# negative if the variable number is negative
# zero if the variable number is equal to zero

some_input = float(input("Enter a number: "))
number = some_input
if number > 0:
    print("Positive Number")
elif number == 0:
    print("Zero")
else:
    print("Negative Number")
