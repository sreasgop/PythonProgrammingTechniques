# QUESTION:
# Frame a class Complex with object variable real and imag. Create multiple complex numbers and display them in the format a+bi. Also, count how many complex numberyou have created by using class variable.



# CODE:
class Complex:

    count = 0

    def __init__(self, real, imag):
        self.real = real 
        self.imag = imag
        Complex.count += 1

    @classmethod
    def get_count(cls):
        return f"\nTotal No. of Complex Numbers: {cls.count}"

    def __str__(self):
        sign = '+' if self.imag >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imag)}i"


c1 = Complex(3, 4)
c2 = Complex(1, -2)
c3 = Complex(0, 7)

print("Complex Numbers:")
print(c1)
print(c2)
print(c3)

print(Complex.get_count())



# OUTPUT:
# Complex Numbers:
# 3 + 4i
# 1 - 2i
# 0 + 7i
#
# Total No. of Complex Numbers: 3
