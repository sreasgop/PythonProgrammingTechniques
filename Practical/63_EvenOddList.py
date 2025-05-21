# QUESTION:
# Write a program that creates a list of ten random integers. Then create two lists- Odd list and Even list that has all odd and even values in the list respectively.



# CODE:
import random

numbers = [random.randint(1, 100) for _ in range(10)]
odd = [num for num in numbers if num % 2 != 0]
even = [num for num in numbers if num % 2 == 0]

print("Original list:", numbers)
print("Odd list:", odd)
print("Even list:", even)



# OUTPUT:
# Original list: [74, 65, 13, 72, 26, 38, 33, 83, 48, 97]
# Odd list: [65, 13, 33, 83, 97]
# Even list: [74, 72, 26, 38, 48]
