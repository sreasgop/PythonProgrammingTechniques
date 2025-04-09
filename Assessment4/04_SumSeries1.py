# QUESTION:
# Write a program to find the sum of the series:
# S = 1 + (1+2) + (1+2+3) + ...... + (1+2+3+..+N)



# CODE:
n = int(input("Enter n: "))

total = 0

for i in range(1, n+1):
    for j in range(1, i+1):
        total += j

print(f"Sum Series: {total}")



# OUTPUT:
# Enter n: 3
# Sum Series: 10
#
# Enter n: 5
# Sum Series: 35
#
# Enter n: 10
# Sum Series: 220
