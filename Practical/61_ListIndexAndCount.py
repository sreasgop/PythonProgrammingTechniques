# QUESTION:
# Write a program to print index at which a particular value exists. If the value exists in multiple locations in the list, then print all the indices. Also count the number of times that value is repeated in the list.



# CODE:
values = [1, 2, 3, 2, 4, 2, 5]
val = int(input("Enter the value to search: "))

indices = [i for i, x in enumerate(values) if x == val]
print("Indices where value exists:", indices)
print("Count of occurrences:", len(indices))



# OUTPUT:
# Enter the value to search: 5
# Indices where value exists: [6]
# Count of occurrences: 1
