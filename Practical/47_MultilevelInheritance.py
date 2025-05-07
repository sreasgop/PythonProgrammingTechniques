# QUESTION:
# Write a program to demonstrate how multilevel inheritance works in Python.



# CODE:
class Animal:
    def sleep(self):
        print("Animal sleeps")

class Dog(Animal):
    def bark(self):
        print("Bark Bark!")

class Puppy(Dog):
    def weep(self):
        print("Weep weep!")

p = Puppy()
p.sleep()
p.bark()
p.weep()



# OUTPUT:
#Animal sleeps
# Bark Bark!
# Weep weep!

