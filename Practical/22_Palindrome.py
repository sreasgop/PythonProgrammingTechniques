# QUESTION: 
# Write a program to check whether a number is a Palindrome or not. 



# CODE:
num = input("Enter a number: ")

if num == num[::-1]:
    print(f"{num} is Palindrome.")
else:
    print(f"{num} is Not Palindrome.")



# OUTPUT: 
# Enter a number: 230032
# 230032 is Palindrome.
