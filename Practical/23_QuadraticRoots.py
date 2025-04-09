# QUESTION:
# Write a program to find the roots of quadratic quation ax^2 + bx + c for all possible combinations of a, b and c.



# CODE: 
import cmath

try:
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    if a == 0:
        if b == 0:
            if c == 0:
                print("All real numbers are solutions (0 = 0).")
            else:
                print("No solution (contradiction: c ≠ 0).")
        else:
            root = -c / b
            print(f"Linear equation. Root: {root:.2f}")
    else:
        d = b**2 - 4*a*c
        root1 = (-b + cmath.sqrt(d)) / (2 * a)
        root2 = (-b - cmath.sqrt(d)) / (2 * a)

        if d == 0:
            print(f"Double root: {root1.real:.2f}")
        elif d > 0:
            print(f"Two real roots: {root1.real:.2f}, {root2.real:.2f}")
        else:
            print(f"Complex roots: {root1:.2f}, {root2:.2f}")

except ValueError:
    print("Error: Please enter valid numbers.")



# OUTPUT: 
# Enter a: 1
# Enter b: -5
# Enter c: 6
# Two real roots: 3.00, 2.00
