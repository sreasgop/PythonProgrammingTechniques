# QUESTION: 
# Swap two integer values without using a third variable.



# CODE:
a = int(input("Enter a: "))
b = int(input("Enter b: "))

a, b = b, a
print("\nAfter Swapping:")
print(f"a: {a}")
print(f"b: {b}")



# OUTPUT:
# Enter a: 10
# Enter b: 5
#
# After Swapping:
# a: 5
# b: 10

