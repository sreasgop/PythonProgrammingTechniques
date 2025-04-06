
calls = int(input("Enter the number of calls made: "))

bill = 100

if calls > 100:
    extra_calls = calls - 100 
    if extra_calls <= 400:
        bill += (extra_calls // 50) * 5
    else:
        bill += (400 // 50) * 5
        bill += (extra_calls - 400) * 1.25


print(f"Total Telephone Bill: Rs. {bill:.2f}")
