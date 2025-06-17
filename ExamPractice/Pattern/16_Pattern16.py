# E
# D E
# C D E
# B C D E
# A B C D E

n = int(input("Enter n: "))
ascii_value = 69

for i in range(1, n+1):
    for j in range(0, i):
        print(chr(ascii_value+j), end=" ")
    ascii_value -= 1
    print()