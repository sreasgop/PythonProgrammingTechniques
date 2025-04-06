# QUESTION:
# Two numbers are input through the keyboard into two locations x and y. Write a program to interchange the contents of x and y. 



# CODE:
x = float(input("Enter value of x: "))
y = float(input("Enter value of y: "))

x, y = y, x

print("\nAfter Swapping: ")
print(f"x = {x}")
print(f"y = {y}")



# OUTPUT:
# Enter value of x: 10
# Enter value of y: 5

# After Swapping:
# x = 5.0
# y = 10.0
