# QUESTION:
# Write a program to print the following pattern for n number of rows (value of n should be user input)



# CODE:
n = int(input("Enter n: "))

for i in range(n):
    for j in range(1, n-i+1):
        print(j, end=" ")
    print()



# OUTPUT: 
# Enter n: 4
# 1 2 3 4
# 1 2 3
# 1 2
# 1
