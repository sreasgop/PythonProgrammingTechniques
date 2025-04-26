# QUESTION:
# 4. Define a function which will compute minimum of three numbers and call the function from main modulel by using keyword arguments to change the positional argument setting and display the result.



# CODE:
def find_min(x, y, z):
    return min(x, y, z)

print("Minimum is:", find_min(x=10, y=5, z=7))
print("Minimum is:", find_min(z=15, x=3, y=20))
print("Minimum is:", find_min(y=8, x=12, z=4))



# OUTPUT:
# Minimum is: 5
# Minimum is: 3
# Minimum is: 4
