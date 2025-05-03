# QUESTION:
# Frame a Student class with object variable student name, roll and marks. Create two student objects and display their details.



# CODE:
class Student:
    def __init__(self, name, roll, marks):
        self.name = name 
        self.roll = roll
        self.marks = marks

    def __str__(self):
        return f"{self.name}, {self.roll}, {self.marks}"

s1 = Student("Arjun", 2490, 90)
s2 = Student("Rahul", 2381, 78)

print(s1)
print(s2)



# OUTPUT:
# Arjun, 2490, 90
# Rahul, 2381, 78
