# A
# AB
# ABC
# ABCD
# ABCDE

def letter_triangle(num):
    for i in range(1, num+1):
        for j in range(0, i):
            print(chr(65+j), end="")
        print()

n = int(input("Enter n: "))
letter_triangle(n)