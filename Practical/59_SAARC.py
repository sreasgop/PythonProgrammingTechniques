# QUESTION:
# Write a program that defines a list of countries that are members of SAARC. Take one country name from user and check whether that country is a member of SAARC or not. 



# CODE:
saarc = ['India', 'Nepal', 'Pakistan','Bangladesh', 'Sri Lanka', 'Afghanistan', 'Bhutan', 'Maldives']
country = input("Enter a country name: ").strip()

if country in saarc:
    print(f"{country} is a SAARC member.")
else:
    print(f"{country} is not a SAARC member.")



# OUTPUT:
# Enter a country name: India
# India is a SAARC member.

# Enter a country name: Canada
# Canada is NOT a SAARC member.
