# QUESTION:
# Write a program to find the sum of the series 1 + 2 + 3 + ---------- + N (value of N should be user input).



# CODE:
n = int(input("Enter n: "))

sum_series = n * (n + 1) / 2
print(f"Sum of first {n} natural numbers: {sum_series}")



# OUTPUT:
# Enter n: 5
# Sum of first 5 natural numbers: 15.0
