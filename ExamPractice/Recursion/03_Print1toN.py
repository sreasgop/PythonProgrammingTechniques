# Print 1 to N using recursion 


def print1toN(start, num):
    if start == num+1: 
        return
    print(start)
    print1toN(start+1, num)

num1 = int(input("Enter n: "))
print1toN(1, num1)