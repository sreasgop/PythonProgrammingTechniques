# Understand recursion by printing something n times 

def printSomething(n):
    if n == 0:
        return
    print("Something")
    printSomething(n-1)

num = int(input("Enter n: "))
printSomething(num)