
def SumOfNum(n):
    if n == 0:
        return 0
    return n + SumOfNum(n-1)

num = int(input("Enter n: "))
print(SumOfNum(num))