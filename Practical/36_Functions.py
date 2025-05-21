# QUESTION:
# Develop a main module using functions where from main module user will call two functions f1() and f2(), f1() will call f3() and f4(), f2() will call f5() and f6(), f3() will call f7() and f6() will call f8().



# CODE:
def f8():
    print("f8() called")

def f7():
    print("f7() called")

def f6():
    print("f6() called")
    f8()

def f5():
    print("f5() called")

def f4():
    print("f4() called")

def f3():
    print("f3() called")
    f7()


def f1():
    print("f1() called")
    f3()
    f4()
    print("\n")


def f2():
    print("f2() called")
    f5()
    f6()
    print("\n")


f1()
f2()



# OUTPUT:
# f1() called
# f3() called
# f7() called
# f4() called
#
#
# f2() called
# f5() called
# f6() called
# f8() called
