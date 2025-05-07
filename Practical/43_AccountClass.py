# QUESTION:
#Frame class Account with object variable account holders name, account number and balance. Create multiple objects of Account class and perform withdraw, deposit and check balance operations on that account. Also, keep track of how many accounts you have created by using a class variable. 



# CODE:
class Account:
    
    count = 0

    def __init__(self, name, account_number, balance):
        self.account_holders_name = name
        self.account_number = account_number
        self.balance = balance
        Account.count += 1

    def get_balance(self):
        print(f"Account Balance of {self.account_holders_name}: {self.balance}\n")

    def deposit(self, amount):
        if amount < 0:
            print("Invalid Amount!")
        self.balance += amount
        print(f"Account no: {self.account_number} credited with amount Rs.{amount}\nCurrent Balance: Rs.{self.balance}.\n")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance in account.")
        else:
            self.balance -= amount
        print(f"Account no: {self.account_number} debited with amount Rs.{amount}\nCurrent Balance: Rs.{self.balance}.\n")

    @classmethod
    def get_count(cls):
        return f"Total No. of accounts created: {cls.count}"

    def __str__(self):
        return f"Account Holder's Name: {self.account_holders_name}\nAccount Number: {self.account_number}\nBalance: {self.balance}\n"



a1 = Account("Chandra Sreas Gop", 2451, 100000)
a2 = Account("Soutrika Das", 2454, 99800)
a3 = Account("Sanjib Kumar Sah", 2492, 70000)

print(a1)
print(a2)
print(a3)

a1.deposit(16000)
a1.withdraw(590)
a1.get_balance()

print(Account.get_count())



# OUTPUT:
# Account Holder's Name: Chandra Sreas Gop
# Account Number: 2451
# Balance: 100000
#
# Account Holder's Name: Soutrika Das
# Account Number: 2454
# Balance: 99800
#
# Account Holder's Name: Sanjib Kumar Sah
# Account Number: 2492
# Balance: 70000
#
# Account no: 2451 credited with amount Rs.16000
# Current Balance: Rs.116000.
#
# Account no: 2451 debited with amount Rs.590
# Current Balance: Rs.115410.
#
# Account Balance of Chandra Sreas Gop: 115410
#
# Total No. of accounts created: 3
