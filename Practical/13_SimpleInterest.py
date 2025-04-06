# QUESTION:
# Write a program to calculate simple interest.



# CODE:
principle = float(input("Enter the principle amount: "))
rate = float(input("Enter the rate of interest: "))
time = int(input("Enter the time period: "))
simple_interest = (principle * rate * time)/100
print(f"Simple Interest: {simple_interest:.3f}")



# OUTPUT:
# Enter the principle amount: 10000
# Enter the rate of interest: 4
# Enter the time period: 2
# Simple Interest: 800.000
