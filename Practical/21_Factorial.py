# QUESTION:
# Write a program to find the factorial of a number. 



# CODE:
num = int(input("Enter number: "))

fact = 1

for i in range(1, num+1):
    fact *= i

print(f"{num}! = {fact}")



# OUTPUT:
# Enter number: 5
# 5! = 120
