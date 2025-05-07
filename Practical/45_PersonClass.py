# QUESTION:
# Frame a base class Person which contains object variable name and age of a person. It should have a display_person() method which will display details of a person. Frame another two classes Student and Teacher ( both should inherit the base class Person) which will contain roll and marks (for Student) and subject and experience (for Teacher). Student class should contain display_student() method which will display student record and Teacher class should contain display_teacher() method which will display teacher record. Write a program in python to test thc above classes.



# CODE:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, roll, marks):
        super().__init__(name, age)
        self.roll = roll
        self.marks = marks

    def display_student(self):
        self.display_person()
        print(f"Roll: {self.roll}, Marks: {self.marks}")


class Teacher(Person):
    def __init__(self, name, age, subject, experience):
        super().__init__(name, age)
        self.subject = subject
        self.experience = experience

    def display_teacher(self):
        self.display_person()
        print(f"Subject: {self.subject}, Experience: {self.experience} years")


s = Student("Alice", 20, 101, 88)
t = Teacher("Mr. Smith", 45, "Math", 15)

print("Student Record:")
s.display_student()

print("\nTeacher Record:")
t.display_teacher()



# OUTPUT:
# Student Record:
# Name: Alice, Age: 20
# Roll: 101, Marks: 88
#
# Teacher Record:
# Name: Mr. Smith, Age: 45
# Subject: Math, Experience: 15 years
