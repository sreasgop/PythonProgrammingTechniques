# QUESTION:
# Frame a class Complex with object variable real and imag. Create two complex numbers and display them in the format a+bi. Add those two complex numbers to get a resultant third complex number and display it in the format a + bi.



# CODE:
class Complex:

    def __init__(self, real, imag):
        self.real = real 
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

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

c4 = c1 + c2
print("\nResult of c1 + c2:")
print(c4)



# OUTPUT:
# Complex Numbers:
# 3 + 4i
# 1 - 2i
# 0 + 7i
#
# Result of c1 + c2:
# 4 + 2i
