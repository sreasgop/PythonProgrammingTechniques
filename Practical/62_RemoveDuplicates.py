# QUESTION:
# Write a program to remove all duplicate objects from a list.



# CODE:
original = [1, 2, 2, 3, 4, 4, 5, 1]
no_duplicates = list(set(original))
print("Original List: ", original)
print("List after removing duplicates:", no_duplicates)



# OUTPUT:
# Original List:  [1, 2, 2, 3, 4, 4, 5, 1]
# List after removing duplicates: [1, 2, 3, 4, 5]
