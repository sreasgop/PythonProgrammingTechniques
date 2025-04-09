# QUESTION:
# Write a program to find out whether a number is prime or not.



# CODE:
from math import sqrt

num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is not prime!")
else:
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            print(f"{num} is not prime.")
            break
    else:
        print(f"{num} is prime.")



# OUTPUT:
# Enter a number: 7
# 7 is prime.
#
# Enter a number: 10
# 10 is not prime.
