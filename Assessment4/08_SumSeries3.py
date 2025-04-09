# QUESTION:
# Write a program to calculate the sum of the following series:
# S = 1/2! - 2/3! + 3/4! - 4/5! + ....... + n(n+1)!



# CODE:
import math

n = int(input("Enter n: "))
total = 0 
sign = 1

for i in range(1, n+1):
    total += sign * i / math.factorial(i+1)
    sign *= -1

print(f"Sum of the series: {total:.5f}")



# OUTPUT:
# Enter n: 3
# Sum of the series: 0.29167

# Enter n: 4
# Sum of the series: 0.25833
