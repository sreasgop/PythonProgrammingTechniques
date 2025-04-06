dip_age = int(input("Enter Dip's age: "))
rahul_age = int(input("Enter Rahul's age: "))
tamal_age = int(input("Enter Tamal's age: "))


youngest = min(dip_age, rahul_age, tamal_age)


if youngest == dip_age:
    print("Dip is the youngest.")
elif youngest == rahul_age:
    print("Rahul is the youngest.")
else:
    print("Tamal is the youngest.")
