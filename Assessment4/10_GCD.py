# QUESTION: 
# Write a program to calculate the gcd (greatest common divisor) of two numbers. 



# CODE:
def gcd(a, b):
    while b: 
        a, b = b, a % b
    return a

num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))

gcd_result = gcd(num1, num2)

print(f"GCD of {num1} and {num2} is: {gcd_result}")



# OUTPUT: 
# Enter first num: 36
# Enter second num: 60
# GCD of 36 and 60 is: 12

