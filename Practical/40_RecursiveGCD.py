# QUESTION:
# Define a recursive function to calculate GCD/HCF of two numbers.



# CODE:
def gcd(a, b):
    if a == b:
        return a
    elif a < b:
        return gcd(b, a)
    else:
        return gcd(b, a - b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"GCD of {num1} and {num2}: {gcd(num1, num2)}")



# OUTPUT:
