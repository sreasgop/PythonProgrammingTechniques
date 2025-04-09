# QUESTION:
# Write a python program to print the following pattern for n number of rows (value of n should be user input)
# *
# ***
# *****
# *******



# CODE:
n = int(input("Enter n: "))

for i in range(1, n+1):
    print("*" * (2 * i - 1))



# OUTPUT:
# *
# ***
# *****
# *******
