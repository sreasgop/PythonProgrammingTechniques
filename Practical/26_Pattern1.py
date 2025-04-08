# QUESTION: 
# Write a program to print a pyramid of digits as shown below for n number of lines.
#       1
#     2 3 2
#   3 4 5 4 3
# 4 5 6 7 6 5 4         (for n = 4)



# CODE:
n = int(input("Enter n: "))

for i in range(1, n+1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(i, 2*i):
        print(j, end=" ")
    for j in range(2*i-2, i-1, -1):
        print(j, end=" ")
    print()



# OUTPUT:
# Enter n: 4
#       1
#     2 3 2
#   3 4 5 4 3
# 4 5 6 7 6 5 4
