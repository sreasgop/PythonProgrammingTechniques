# QUESTION:
# Write a program to calculate simple interest (principle, time and rate of interest will be user input).



# CODE:
principle = float(input("Enter the principle amount: "))
rate = float(input("Enter the rate of interest: "))
time = int(input("Enter the time period (in years): "))
simple_interest = (principle * rate * time)/100
print(f"Simple Interest: {simple_interest:.3f}")



# OUTPUT:
# Enter the principle amount: 10000
# Enter the rate of interest: 4
# Enter the time period (in years): 2
# Simple Interest: 800.000
