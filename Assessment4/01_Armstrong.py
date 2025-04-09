# QUESTION:
# Write a program to generate all the Armstrong numbers between 1 to 1000. 



# CODE:
def is_armstrong(num):
    if sum(int(digit) ** len(str(num)) for digit in str(num)) == num:
        flag = True
    else:
        flag = False

    return flag


for i in range(1, 1000):
    if is_armstrong(i):
        print(i, end=" ")



# OUTPUT:
# 1 2 3 4 5 6 7 8 9 153 370 371 407
