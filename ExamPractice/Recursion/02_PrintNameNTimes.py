# Print Name n Times using recursion

def printName(n, name):
    if n == 0:
        return
    print(name)
    printName(n-1, name)

num = int(input("Enter n: "))
name1 = input("Enter name: ")
printName(num, name1)