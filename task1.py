#!python3 

"""
##### Task 1
Ask the user to enter an integer.
Print the multiplication tables up to 12 for that number
using a for loop instead of a while loop.
(2 points)

inputs:
int number

outputs:
multiples of that number

example:
Enter number:4
4 8 12 16 20 24 28 32 36 40 44 48
"""
number = int(input("Enter a number"))
mnumber = int(number * 12)
numbs = range(1,13)
for x in numbs:
    print(x * number, end = " ")
