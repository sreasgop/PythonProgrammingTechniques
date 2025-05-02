# QUESTION:
# 5. Define a function which will accept name of a student and a set of sports that he/she likes and this function will display the student name and his/her favorite sports. Use variable length argument in the function parameter so that different student can have different number of favorite sports.



# CODE:
def student_sports(name, *sports):
    print(f"Student Name: {name}")
    print("Favorite Sports:", ", ".join(sports))
    print()

student_sports("Arjun", "Cricket", "Football", "Badminton")
student_sports("Priya", "Tennis")
student_sports("Raj", "Hockey", "Chess", "Kabaddi", "Swimming")



# OUTPUT 
# Student Name: Arjun
# Favorite Sports: Cricket, Football, Badminton
#
# Student Name: Priya
# Favorite Sports: Tennis
#
# Student Name: Raj
# Favorite Sports: Hockey, Chess, Kabaddi, Swimming
