# QUESTION:
# Write a program to find the roots of quadratic quation ax^2 + bx + c for all possible combinations of a, b and c.



# CODE: 
import cmath

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = b**2 - 4*a*c

root1 = (-b + cmath.sqrt(d)) / (2 * a)
root2 = (-b - cmath.sqrt(d)) / (2 * a)

print(f"Roots are: {root1} and {root2}")



# OUTPUT: 
# Enter a: 1
# Enter b: -5
# Enter c: 6
# Roots are: (3+0j) and (2+0j)
