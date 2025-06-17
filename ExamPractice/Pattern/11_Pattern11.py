# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

n = int(input("Enter n: "))

value = 1

for i in range(1, n+1):
    for j in range(1, i+1):
        print(value, end=" ")
        if value == 1: 
            value = 0
        else: 
            value = 1
    if i % 2 == 0: 
        value = 1
    print()