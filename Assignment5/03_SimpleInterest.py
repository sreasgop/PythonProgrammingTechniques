# QUESTION:
# 3. Define a function which will take principal amount, time in years and rate of interest in percentage as input and calculate the simple interest. All the three arguments have default values — 1000 (principal amount), 5 (time in years) and IO (rate of interest in percentage). Call the function from main module with all possible ways and calculate the simple interest each time.



# CODE:
def simple_interest(principal=1000, time=5, rate=10):
    return (principal * time * rate) / 100

print("Using Default Value Arguments:")
print("Simple Interest:", simple_interest())
print()

print("\nUsing Positional Arguments:")
print("Simple Interest:", simple_interest(100000, 2, 8.5))
print()

print("\nUsing Keyword Arguments:")
p = float(input("Enter principal amount: "))
print("Simple Interest (principle only):", simple_interest(principal=p))

p = float(input("\nEnter principal amount: "))
t = int(input("Enter time in years: "))
print("Simple Interest (principal and time):", simple_interest(principal=p, time=t))

# Passing all three arguments
p = float(input("\nEnter principal amount: "))
t = int(input("Enter time in years: "))
r = float(input("Enter rate of interest: "))
print("Simple Interest (all arguments):", simple_interest(principal=p, time=t, rate=r))



# OUTPUT:
# Using Default Value Arguments:
# Simple Interest: 500.0
#
#
# Using Positional Arguments:
# Simple Interest: 17000.0
#
#
# Using Keyword Arguments:
# Enter principal amount: 10000
# Simple Interest (principle only): 5000.0
#
# Enter principal amount: 100000
# Enter time in years: 2
# Simple Interest (principal and time): 20000.0
#
# Enter principal amount: 100000
# Enter time in years: 1
# Enter rate of interest: 8.5
# Simple Interest (all arguments): 8500.0
