# QUESTION: 
# Write a program to calculate sum of digits of a number. 



# CODE: 
num = input("Enter the number: ")
sum_of_digits = sum(int(digit) for digit in num)

print(f"Sum of digits of {num}: {sum_of_digits}")



# OUTPUT: 
# Enter the number: 12345
# Sum of digits of 12345: 15
