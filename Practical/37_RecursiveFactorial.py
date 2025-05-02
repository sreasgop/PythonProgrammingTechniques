# QUESTION:
# Define a recursive function that will calculate factorial of number. Develop the program from main module.



# CODE:
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

n = int(input("Enter n: "))
print(f"{n}! = {factorial(n)}")



# OUTPUT:
# Enter n: 5
# 5! = 120
