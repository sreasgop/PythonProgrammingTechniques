full_mark = float(input("Enter Full Marks: "))

print("\nEnter Obtained Marks:")
sub1 = float(input("Subject 1: "))
sub2 = float(input("Subject 2: "))
sub3 = float(input("Subject 3: "))

percentage = ((sub1 + sub2 + sub3) / (full_mark * 3)) * 100

if percentage >= 60:
    print("First division")
elif 50 <= percentage < 60:
    print("Second division")
elif 40 <= percentage < 50:
    print("Third division")
else:
    print("Fail")
