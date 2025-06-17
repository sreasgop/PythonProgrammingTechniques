# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

count = 1

def pattern(num):
    global count
    for i in range(num):
        for j in range(i+1):
            print(count, end=" ")
            count += 1
        print()

n = int(input("Enter n: "))
pattern(n)