# QUESTION:
# Write a program to generate all odd non prime numbers between 10 to 100



# CODE:
from math import sqrt

print("All odd non-prime numbers between 10 - 100:")
for i in range(10, 101):
    if i % 2 != 0:
        for j in range(2, int(sqrt(i))+1):
            if i % j == 0:
                print(i, end=" ")
                break



# OUTPUT:
# All odd non-prime numbers between 10 - 100:
# 15 21 25 27 33 35 39 45 49 51 55 57 63 65 69 75 77 81 85 87 91 93 95 99
