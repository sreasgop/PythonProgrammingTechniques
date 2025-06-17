#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *

def upper_pyramid(n):
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end="")
        for k in range(i*2-1):
            print("*", end="")
        print()

def lower_pyramid(n):
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for j in range(n*2-1 - i*2):
            print("*", end="")
        print()

def diamond(n):
    upper_pyramid(n)
    lower_pyramid(n)


num = int(input("Enter n: "))
diamond(num)
