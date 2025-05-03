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
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        print(f"Account no: {self.account_number} successfully deposited with amount Rs.{amount}\nTotal Balance: Rs.{self.balance}\n")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance in account.")
        else:
            self.balance -= amount
    
    @classmethod
    def get_count(cls):
        return cls.count

    def __str__(self):
        return f"Account Holder's Name: {self.account_holders_name}\nAccount Number: {self.account_number}\nBalance: {self.balance}\n"


a1 = Account("Chandra Sreas Gop", 2451, 100000)
a2 = Account("Soutrika Das", 2454, 99800)
a3 = Account("Sanjib Kumar Sah", 2492, 70000)

a1.deposit(16000)

print(a1)
print(a2)
print(a3)
print("No of Accounts:", Account.get_count())
