# QUESTION:
# Ramesh's basic salary is input through the keyboard. His DA is 40% of basic salary, HRA is 20% of basic salary and MA is Rs. 300. Write a program to calculate his gross salary. 



# CODE:
basic_salary = float(input("Enter basic salary: "))
da = (basic_salary * 40)/100
hra = (basic_salary * 20)/100
ma = 300
gross_salary = basic_salary + da + hra + ma
print(f"Gross Salary: {gross_salary:.3f}")



# OUTPUT:
# Enter basic salary: 10000
# Gross Salary: 16300.000
