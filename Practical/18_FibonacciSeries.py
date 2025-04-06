# QUESTION:
# Write a program to generate Fibonacci series upto N terms (value of N should be user input).



# CODE:
n = int(input("Enter n: "))

first_term = 0
second_term = 1
next_term = 0

for i in range(n):
    print(f"{next_term}", end=" ")
    first_term = second_term 
    second_term = next_term 
    next_term = first_term + second_term 

print()



# OUTPUT: 
# Enter n: 8
# 0 1 1 2 3 5 8 13
