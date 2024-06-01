# Finger Exercise Lecture 2
# Name: Julian Drangosch
# Collaborator: ---
# Time Spent: 1 min

# ---------- SEPARATOR -------------

# Assume you are given a variable named number (has a numerical value). 
# Write a piece of Python code that prints out one of the following strings: 

# positive if the variable number is positive
# negative if the variable number is negative
# zero if the variable number is equal to zero
number = int(input('Type a number: '))
if number == 0:
    print('zero')
elif number > 0:
    print('positive')
else:
    print('negative')