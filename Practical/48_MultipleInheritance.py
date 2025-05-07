# QUESTION:
# Write a program to demonstrate how multiple inheritance works in Python.



# CODE:
class Father:
    def skills(self):
        print("Gardening, Driving")

class Mother:
    def skills(self):
        print("Cooking, Teaching")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Drawing, Coding")

c = Child()
c.skills()



# OUTPUT:
# Gardening, Driving
# Cooking, Teaching
# Drawing, Coding
