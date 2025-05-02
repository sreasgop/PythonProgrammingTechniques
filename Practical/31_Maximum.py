# QUESTION:
# 1. Define a function which will compute maximum of two numbers and call the function two times from main module with two different sets of values taken from user.



# CODE:
def find_max(a, b):
    return max(a, b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Maximum is:", find_max(num1, num2))

num3 = int(input("\nEnter number: "))
num4 = int(input("Enter another number: "))
print("Maximum is:", find_max(num3, num4))



# OUTPUT:
# Enter first number: 15
# Enter second number: 50
# Maximum is: 50
#
# Enter number: 5
# Enter another number: 10
# Maximum is: 10
