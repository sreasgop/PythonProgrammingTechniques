# QUESTION:
# Write a program to find largest value in a list using reduce() function.



# CODE:
from functools import reduce

numbers = [13, 10, 5, 30, 25, 100, 60, 99, 23]
largest = reduce(lambda x, y: x if x > y else y, numbers)
print("Largest value:", largest)



# # OUTPUT:
# Largest value: 100
