# QUESTION:
# Define a recursive function to find out sum of digits of a number (number should be user input).



# CODE:
def sum_of_digits(num):
    if num == 0:
        return 0
    else:
        return num % 10 + sum_of_digits(num//10)

n = int(input("Enter a number: "))
print(f"Sum of digits: {sum_of_digits(n)}")



# OUTPUT:
# Enter a number: 12345
# Sum of digits: 15
