# Write a program to calculate the sum of the digits of a number repeatedly until the sum converts to a single digit. [2347 -> 2 + 3 + 4 + 7 = 16 -> 1 + 6 = 7]



# CODE: 
num = int(input("Enter the number: "))

while num >= 10:
    num = sum(int(digit) for digit in str(num))

print(f"Repeated sum of digits: {num}")



# OUTPUT:
# Enter the number: 2347
# Repeated sum of digits: 7
