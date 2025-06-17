# A
# BB
# CCC
# DDDD
# EEEEE

def letter_pattern(num):
    for i in range(0, num):
        for j in range(0, i+1):
            print(chr(65+i), end="")
        print()

n = int(input("Enter n: "))
letter_pattern(n)