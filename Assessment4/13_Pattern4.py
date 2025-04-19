# QUESTION:
# Write a program to print the following pattern for n number of rows (value of n should be user input)



# CODE:
n = int(input("Enter n: "))

for i in range(1, n+1):
    print(" " * (n-i), end=" ")
    print("*" * (i*2-1), end=" ")
    print()



# OUTPUT:
# Enter n: 4
#     *
#    ***
#   *****
#  *******
