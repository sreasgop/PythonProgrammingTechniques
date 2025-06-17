def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

# Alternate Logic
# def new_gcd(a, b):
#     if a == b: 
#         return a 
#     elif a < b: 
#         return gcd(b, a)
#     else: 
#         return gcd(b, a - b)

def lcm(a, b):
    return abs(a * b)//gcd(a, b)

a = int(input("Enter num: "))
b = int(input("Enter another num: "))

print(gcd(a, b))
# print(new_gcd(a, b))
print(lcm(a, b))