#import for random number generator
from random import randint

class BankAccount:
    #class variables
    routing_number = 123456789
    
    #initialize the class
    def __init__(self, full_name=''):
        #instance variable
        self.name = full_name
        #random 8 digit number
        self.account_number = randint(10000000, 99999999)
        self.balance = 0

    #function to deposit money into balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        print (f"Amount Deposited: ${amount}")
    
    #function to withdraw money from balance
    def withdraw(self, amount):
        #if there isn't enough money, subtract the amount and subtract an additional $10 for overdraft
        if amount > self.balance:
            self.balance = self.balance - amount - 10
            print(f"Amount Withdrawn: ${amount}")
            print("Insufficient funds. Overdraft Fee: $10")
        else:
            self.balance = self.balance - amount
            print(f"Amount Withdrawn: ${amount}")
    
    #function to return the balance 
    def get_balance(self):
        print(f"Your current balance is ${self.balance}.")
        return self.balance

    #adds interest to the total balance
    def add_interest(self):
        self.balance = self.balance + self.balance*0.00083
    
    #function to neatly print all the important information on the bank account 
    def print_receipt(self):
        print(self.name)
        print(f"Account No.: ****{self.account_number%10000}")
        print(f"Routing No.: {self.routing_number}")
        print(f"Balance: ${self.balance}")
    
Swayam = BankAccount("Swayam Barik")
Swayam.deposit(100.10)
Swayam.withdraw(10)
Swayam.add_interest()
Swayam.get_balance()
Swayam.print_receipt()

Kiran = BankAccount("Kiran Barik")
Kiran.deposit(90.10)
Kiran.withdraw(100)
Kiran.print_receipt()

Josh = BankAccount("Josh Haynes")
Josh.deposit(100000.10)
Josh.withdraw(638.92)
Josh.add_interest()
Josh.print_receipt()