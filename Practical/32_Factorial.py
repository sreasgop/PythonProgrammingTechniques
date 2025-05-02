# QUESTION:
# 2. Define a function which will calculate factorial of a number and call the function from main module with a value taken from user.



# CODE:
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

number = int(input("Enter a number to calculate factorial: "))
print(f"{number} ! = ", factorial(number))



# OUTPUT:
# Enter a number to calculate factorial: 5
# 5 ! =  120 
