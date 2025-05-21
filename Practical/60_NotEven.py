# QUESTION:
# Write a program to create a list of numbers in the range 1 to 10. Then delete all the even numbers from the list and print the final list.



# CODE:
numbers = list(range(1, 11))
numbers = [num for num in numbers if num % 2 != 0]
print("Final list:", numbers)



# OUTPUT:
# Final list: [1, 3, 5, 7, 9]
