# QUESTION:
# Define a recursive function that will calculate Fibonacci number for nth term (the value of n should be user input). Develop a program from main module using that function to display the Fibonacci series for n term.



# CODE:
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

n = int(input("Enter n: "))
print(f"{n}th Fibonacci Term: {fibonacci(n)}")



# OUTPUT:
# Enter n: 8
# 8th Fibonacci Term: 21
