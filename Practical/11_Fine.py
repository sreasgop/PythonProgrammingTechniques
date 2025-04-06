days_late = int(input("Enter the number of days the book is returned late: "))

if days_late <= 5:
    fine = days_late * 0.50  
elif 6 <= days_late <= 10:
    fine = days_late * 1 
elif 11 <= days_late <= 30:
    fine = days_late * 5  
else:
    print("Membership cancelled due to delay beyond 30 days.")
    fine = None

if fine is not None:
    print(f"Fine to be paid: Rs {fine:.2f}")