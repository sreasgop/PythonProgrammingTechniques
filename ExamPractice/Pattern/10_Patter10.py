# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

def upper_triangle(num):
    for i in range(num):
        for j in range(i+1):
            print("*", end="")
        print()

def lower_triangle(num):
    for i in range(1, num):
        for j in range(n-i):
            print("*", end="")
        print()

def right_arrow_pattern(num):
    upper_triangle(num)
    lower_triangle(num)


n = int(input("Enter n: "))
# lower_triangle(n)


right_arrow_pattern(n)